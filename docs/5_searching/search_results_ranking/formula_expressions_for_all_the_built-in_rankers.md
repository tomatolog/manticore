### Formula expressions for all the built-in rankers {#formula-expressions-for-all-the-built-in-rankers}

Most of the other rankers can actually be emulated with the expression based ranker. You just need to pass a proper expression. Such emulation is, of course, going to be slower than using the built-in, compiled ranker but still might be of interest if you want to fine-tune your ranking formula starting with one of the existing ones. Also, the formulas define the nitty gritty ranker details in a nicely readable fashion.

*   SPH_RANK_PROXIMITY_BM25 = sum(lcs*user_weight)*1000+bm25

*   SPH_RANK_BM25 = bm25

*   SPH_RANK_NONE = 1

*   SPH_RANK_WORDCOUNT = sum(hit_count*user_weight)

*   SPH_RANK_PROXIMITY = sum(lcs*user_weight)

*   SPH_RANK_MATCHANY = sum((word_count+(lcs-1)*max_lcs)*user_weight)

*   SPH_RANK_FIELDMASK = field_mask

*   SPH_RANK_SPH04 = sum((4*lcs+2*(min_hit_pos==1)+exact_hit)*user_weight)*1000+bm25