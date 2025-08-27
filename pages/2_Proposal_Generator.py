import streamlit as st
# {k['project']} — Proposal Draft
Organization: {k['org']}


## Summary
{k['summary']}


## Needs Statement
{k['need']}


## Goals & Objectives
{k['goals']}


## Methods / Activities
{k['methods']}


## Evaluation
{k['evaln']}


## Budget
{k['budget']}


## Sustainability
{k['sustain']}


## Alignment with Tribal Sovereignty & Culture
{k['sovereignty']}
"""


if use_ai:
client = get_client()
try:
base_text = assemble_text(org=org, project=project, summary=summary, need=need, goals=goals, methods=methods, evaln=evaln, budget=budget, sustain=sustain, sovereignty=sovereignty)
prompt = (
"Improve and expand the following grant proposal sections for clarity, structure, and persuasive impact. "
"Keep culturally respectful language and align with Tribal sovereignty. Return clean Markdown.\n\n" + base_text
)
resp = client.chat.completions.create(
model=st.secrets.get("OPENAI_MODEL", "gpt-4o-mini"),
messages=[{"role":"user","content": prompt}]
)
final_md = resp.choices[0].message.content
except Exception as e:
st.error(f"OpenAI error: {e}")
final_md = assemble_text(org=org, project=project, summary=summary, need=need, goals=goals, methods=methods, evaln=evaln, budget=budget, sustain=sustain, sovereignty=sovereignty)
else:
final_md = assemble_text(org=org, project=project, summary=summary, need=need, goals=goals, methods=methods, evaln=evaln, budget=budget, sustain=sustain, sovereignty=sovereignty)


st.markdown("---")
st.subheader("Draft Preview")
st.markdown(final_md)


# Download as .docx
doc = Document()
for line in final_md.split("\n"):
if line.startswith("# "):
doc.add_heading(line[2:].strip(), level=1)
elif line.startswith("## "):
doc.add_heading(line[3:].strip(), level=2)
else:
doc.add_paragraph(line)
bio = BytesIO()
doc.save(bio)
st.download_button("Download .docx", data=bio.getvalue(), file_name=f"{project or 'proposal'}.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")


st.sidebar.page_link("streamlit_app.py", label="🏠 Home")
