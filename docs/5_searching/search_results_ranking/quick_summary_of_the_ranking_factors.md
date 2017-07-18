### Quick summary of the ranking factors {#quick-summary-of-the-ranking-factors}

Table 5.1. 

| Name | Level | Type | Summary |
| --- | --- | --- | --- |
| max_lcs | query | int | maximum possible LCS value for the current query |
| bm25 | document | int | quick estimate of BM25(1.2, 0) without syntax support |
| bm25a(k1, b) | document | int | precise BM25() value with configurable K1, B constants and syntax support |
| bm25f(k1, b, {field=weight, ...}) | document | int | precise BM25F() value with extra configurable field weights |
| field_mask | document | int | bit mask of matched fields |
| query_word_count | document | int | number of unique inclusive keywords in a query |
| doc_word_count | document | int | number of unique keywords matched in the document |
| lcs | field | int | Longest Common Subsequence between query and document, in words |
| user_weight | field | int | user field weight |
| hit_count | field | int | total number of keyword occurrences |
| word_count | field | int | number of unique matched keywords |
| tf_idf | field | float | sum(tf*idf) over matched keywords == sum(idf) over occurrences |
| min_hit_pos | field | int | first matched occurrence position, in words, 1-based |
| min_best_span_pos | field | int | first maximum LCS span position, in words, 1-based |
| exact_hit | field | bool | whether query == field |
| min_idf | field | float | min(idf) over matched keywords |
| max_idf | field | float | max(idf) over matched keywords |
| sum_idf | field | float | sum(idf) over matched keywords |
| exact_order | field | bool | whether all query keywords were a) matched and b) in query order |
| min_gaps | field | int | minimum number of gaps between the matched keywords over the matching spans |
| lccs | field | int | Longest Common Contiguous Subsequence between query and document, in words |
| wlccs | field | float | Weighted Longest Common Contiguous Subsequence, sum(idf) over contiguous keyword spans |
| atc | field | float | Aggregate Term Closeness, log(1+sum(idf1*idf2*pow(distance, -1.75)) over the best pairs of keywords |