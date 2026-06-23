import streamlit as st

from services.search_service import search_web
from services.research_service import generate_research
from services.blog_service import generate_blog
from services.linkedin_service import generate_linkedin
from services.pdf_service import create_pdf

st.set_page_config(
    page_title="ResearchGPT",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 ResearchGPT")
st.write("AI-Powered Research Assistant")

topic = st.text_input(
    "Enter a Topic",
    placeholder="Example: Blockchain in Real Estate"
)

tab1, tab2, tab3 = st.tabs(
    ["Research", "Blog", "LinkedIn"]
)

# =====================
# RESEARCH TAB
# =====================
with tab1:

    st.subheader("Research Report")

    if st.button("Generate Research"):

        if topic:

            try:

                with st.spinner(
                    "Searching and researching..."
                ):

                    search_results = search_web(
                        topic
                    )

                    if not search_results:

                        st.error(
                            "No search results found."
                        )

                    else:

                        report = generate_research(
                            topic,
                            search_results
                        )

                        st.session_state[
                            "report"
                        ] = report

                        st.session_state[
                            "sources"
                        ] = search_results

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )

        else:

            st.warning(
                "Please enter a topic."
            )

    if "report" in st.session_state:

        st.write(
            st.session_state["report"]
        )

        pdf_file = create_pdf(
            topic,
            st.session_state["report"]
        )

        with open(
            pdf_file,
            "rb"
        ) as file:

            st.download_button(
                label="📄 Download PDF",
                data=file,
                file_name=f"{topic}.pdf",
                mime="application/pdf"
            )

        st.subheader("Sources")

        for source in st.session_state[
            "sources"
        ]:

            st.markdown(
                f"### {source['title']}"
            )

            st.markdown(
                f"[Open Source]({source['url']})"
            )

            st.write(
                source["content"]
            )

            st.divider()

# =====================
# BLOG TAB
# =====================
with tab2:

    st.subheader("Blog Generator")

    if st.button("Generate Blog"):

        if topic:

            try:

                with st.spinner(
                    "Writing blog..."
                ):

                    blog = generate_blog(
                        topic
                    )

                    st.session_state[
                        "blog"
                    ] = blog

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )

        else:

            st.warning(
                "Please enter a topic."
            )

    if "blog" in st.session_state:

        st.write(
            st.session_state["blog"]
        )

# =====================
# LINKEDIN TAB
# =====================
with tab3:

    st.subheader(
        "LinkedIn Post Generator"
    )

    if st.button(
        "Generate LinkedIn Post"
    ):

        if topic:

            try:

                with st.spinner(
                    "Creating LinkedIn post..."
                ):

                    linkedin_post = (
                        generate_linkedin(
                            topic
                        )
                    )

                    st.session_state[
                        "linkedin"
                    ] = linkedin_post

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )

        else:

            st.warning(
                "Please enter a topic."
            )

    if "linkedin" in st.session_state:

        st.write(
            st.session_state[
                "linkedin"
            ]
        )