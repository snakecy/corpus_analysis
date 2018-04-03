首先利用python wordsegment.py icwb2-data/testing/msr_test.utf8 > msr_tool.utf8 然后执行：
perl scripts/score gold/msr_training_words.utf8 gold/msr_test_gold.utf8 ../msr_tool.utf8 > score.ut8
首先利用python wordsegment.py icwb2-data/testing/pku_test.utf8 > pku_tool.utf8 然后执行：
perl scripts/score gold/pku_training_words.utf8 gold/pku_test_gold.utf8 ../pku_tool.utf8 > score.ut8
