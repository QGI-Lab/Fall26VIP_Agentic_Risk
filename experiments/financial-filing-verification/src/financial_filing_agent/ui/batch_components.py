"""Batch interface, kept separate from the single-run form."""
import json
import re
import streamlit as st

from ..config.formulas import FORMULAS
from ..services.batch import BatchRunner, batch_csv


def show_batch(settings):
    with st.expander("Batch: multiple tickers and metrics"):
        st.caption("Fetch each ticker's latest SEC 10-K and run the ordinary evidence pipeline for each metric. "
                   "Results retain their own fiscal years, period end, accession and audit. No analyst or AI comparison is run.")
        with st.form("batch_analysis"):
            ticker_text = st.text_input("Batch ticker symbols", placeholder="TSLA AAPL MSFT")
            metrics = st.multiselect("Batch metrics", list(FORMULAS), default=["current_ratio_change", "inventory_growth"])
            policy = st.selectbox("Batch fiscal-period policy", ["Latest filing fiscal years", "Explicit common fiscal years"])
            year_text = st.text_input("Batch explicit fiscal years", placeholder="FY2025 FY2024")
            submitted = st.form_submit_button("Run Batch")
        if submitted:
            st.session_state.pop("batch_result", None)
            if policy == "Latest filing fiscal years" and year_text.strip():
                st.error("Choose Explicit common fiscal years to use the entered years; they will not be silently ignored.")
            else:
                with st.status("Starting batch…", expanded=True) as status:
                    def progress(event):
                        phase = event["phase"]
                        prefix = event["ticker"] + " / " + event.get("formula_id", "10-K")
                        if phase == "source_started":
                            status.write(prefix + ": resolving and loading latest 10-K")
                        elif phase == "source_completed":
                            status.write(prefix + (": source ERROR" if event.get("error") else ": HTML ready"))
                        elif phase == "item_started":
                            status.update(label=prefix + " / " + " ".join(event["periods"]))
                        elif phase == "completed":
                            status.write(prefix + ": " + event["label"] + " — " + event["detail"])
                        elif phase == "item_completed":
                            status.write(prefix + ": " + event["status"])
                    try:
                        result = BatchRunner(settings).run(re.split(r"[,;\s]+", ticker_text), metrics,
                            year_text.split() if policy == "Explicit common fiscal years" else None, progress)
                    except Exception as exc:
                        status.update(label="Batch error", state="error")
                        st.error(str(exc))
                    else:
                        st.session_state.batch_result = result
                        status.update(label="Batch completed: " + str(result["outcomes"]),
                                      state="error" if result["outcomes"].get("ERROR") else "complete")
        if "batch_result" in st.session_state:
            result = st.session_state.batch_result
            st.caption("Recorded Qwen mode: " + ("enabled" if result["qwen_enabled"] else "disabled"))
            st.dataframe([{k: item.get(k) for k in ("ticker", "formula_id", "periods", "status", "value", "unit", "period_end", "accession", "decoder_calls", "corrections", "seconds")}
                          for item in result["items"]], use_container_width=True)
            st.download_button("Download batch JSON", json.dumps(result, indent=2), "batch-" + result["batch_id"] + ".json")
            st.download_button("Download batch CSV", batch_csv(result["items"]).encode("utf-8-sig"), "batch-" + result["batch_id"] + ".csv")
            with st.expander("Batch evidence and errors"):
                st.json(result)
