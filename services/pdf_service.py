from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

def create_pdf(
    topic,
    content,
    filename="report.pdf"
):

    doc = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            f"Research Report: {topic}",
            styles["Title"]
        )
    )

    story.append(
        Spacer(1, 12)
    )

    story.append(
        Paragraph(
            content,
            styles["BodyText"]
        )
    )

    doc.build(story)

    return filename