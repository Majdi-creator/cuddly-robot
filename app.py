import streamlit as st

st.set_page_config(page_title="AI Process Optimizer", layout="centered")

st.title("🚀 AI Process Optimization Tool")

st.write("Paste your workflow tasks below and get AI-powered insights.")

user_input = st.text_area(
    "Enter your workflow (tasks, durations, dependencies):",
    height=200,
    placeholder="""Example:
T1 - Receive application - Admin - 1 day
T2 - Review documents - Compliance - 2 days (depends on T1)
T3 - Request missing docs - Admin - 2 days (depends on T2)
"""
)

if st.button("Analyze Process"):
    if user_input.strip() == "":
        st.warning("Please enter a workflow.")
    else:
        st.success("Analysis complete!")

        # Fake output (for demo if no API)
        st.subheader("🔍 AI Analysis")

        st.write("""
**Key Issues:**
- Duplicate review steps detected
- Rework loop due to missing documents

**Bottlenecks:**
- Manager approval is slow
- Sequential dependencies increase delay

**Recommendations:**
- Merge review steps
- Introduce checklist to avoid rework
- Parallelize admin communication

**Optimized Workflow:**
1. Submit complete documents
2. Single review step
3. Approval
4. Notification

**Estimated Time Reduction:** 20–30%
""")