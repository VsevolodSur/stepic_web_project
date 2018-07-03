USE stepic;
update qa_question set rating = char_length(title);
commit;
