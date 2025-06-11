# Task and behaviour
In this image should be math theory, with equations and annotations.
Your task is to transcribe it as accurately as possible in a LaTeX document.

- If you encounter what seems to be a mathematical error or sign error, **always** assume it's an error on your side and transcribe it **as is** without correcting it.
- If you encouter what seems to be a logical error in the reasoning, **always** assume it's an error on your side and transcribe it **as is** without correcting it.
- You must not translate any text.
- You must stay as minimalist as possible, while also returning the complete reasoning.
- You will sometime encounter side notes or bits of reasoning that are not complete, you can rephrase it into a valid math step. It is the **only** context in which you are authorized to transcribe something that is not directly on the paper.

# format precisions
- Every line of the reasoning should be contained in a latex \[ \] bloc to maximise step clarity.
- Every number decimals must be points, even if written as a comma on the sheet.
- Every character that can be written in a single character instead of a latex symbol **must** be written as a single character (for example: "\left(" must never appear, simply use "(" instead)
- Every text annotation must be contained in a latex \text{} bloc.
- Bold, italic, or underlined text must be transcribed as normal text.

# LaTeX output
```latex
\documentclass{article}