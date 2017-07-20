Summary
=======
.. toctree::
    1_introduction/about
    1_introduction/sphinx_features
    1_introduction/where_to_get_sphinx
    1_introduction/license
    1_introduction/credits
    1_introduction/history
    2_installation/README
    2_installation/supported_systems
	2_installation/compiling_sphinx_from_source/README
	2_installation/compiling_sphinx_from_source/required_tools
	2_installation/compiling_sphinx_from_source/compiling_on_linux
	2_installation/compiling_sphinx_from_source/known_compilation_issues
	
Installing Sphinx packages on Debian and
   Ubuntu 2_installation/installing_sphinx_packages_on_debian_and_ubuntu
    Installing Sphinx packages on RedHat and
   CentOS 2_installation/installing_sphinx_packages_on_redhat_and_centos
    Installing Sphinx on
   Windows 2_installation/installing_sphinx_on_windows
    Sphinx deprecations and changes in default
   configuration 2_installation/sphinx_deprecations_and_changes_in_default_configu
    Quick Sphinx usage
   tour 2_installation/quick_sphinx_usage_tour
    3. Indexing 3_indexing/README
    Data sources 3_indexing/data_sources
    Full-text fields 3_indexing/full-text_fields
    Attributes 3_indexing/attributes
    MVA (multi-valued
   attributes) 3_indexing/mva_multi-valued_attributes
    Indexes 3_indexing/indexes
    Restrictions on the source
   data 3_indexing/restrictions_on_the_source_data
    Charsets, case folding, translation tables, and replacement
   rules 3_indexing/charsets,_case_folding,_translation_tables,_and_re
    SQL data sources (MySQL,
   PostgreSQL) 3_indexing/sql_data_sources_mysql,_postgresql
    xmlpipe2 data source 3_indexing/xmlpipe2_data_source
    tsvpipe:raw-latex:`\csvpipe `(Tab:raw-latex:`\Comma `Separated
   Values) data
   source 3_indexing/tsvpipecsvpipe_tabcomma_separated_values_data_sour
    Live index updates 3_indexing/live_index_updates
    Delta index updates 3_indexing/delta_index_updates
    Index merging 3_indexing/index_merging
    4. Real-time indexes 4_real-time_indexes/README
    RT indexes overview 4_real-time_indexes/rt_indexes_overview
    Known caveats with RT
   indexes 4_real-time_indexes/known_caveats_with_rt_indexes
    RT index internals 4_real-time_indexes/rt_index_internals
    Binary logging 4_real-time_indexes/binary_logging
    5. Searching 5_searching/README
    Matching modes 5_searching/matching_modes
    Boolean query syntax 5_searching/boolean_query_syntax
    Extended query syntax 5_searching/extended_query_syntax
    Search results
   ranking 5_searching/search_results_ranking/README

       Ranking
      overview 5_searching/search_results_ranking/ranking_overview
       Available built-in
      rankers 5_searching/search_results_ranking/available_built-in_rankers
       Expression based ranker
      (SPH\_RANK\_EXPR) 5_searching/search_results_ranking/expression_based_ranker_sphrank_expr
       Quick summary of the ranking
      factors 5_searching/search_results_ranking/quick_summary_of_the_ranking_factors
       Document-level ranking
      factors 5_searching/search_results_ranking/document-level_ranking_factors
       Field-level ranking
      factors 5_searching/search_results_ranking/field-level_ranking_factors
       Ranking factor aggregation
      functions 5_searching/search_results_ranking/ranking_factor_aggregation_functions
       Formula expressions for all the built-in
      rankers 5_searching/search_results_ranking/formula_expressions_for_all_the_built-in_rankers

    Expressions, functions, and
   operators 5_searching/expressions,_functions,_and_operators/README.5

       Operators 5_searching/expressions,_functions,_and_operators/operators
       Numeric
      functions 5_searching/expressions,_functions,_and_operators/numeric_functions
       Date and time
      functions 5_searching/expressions,_functions,_and_operators/date_and_time_functions
       Type conversion
      functions 5_searching/expressions,_functions,_and_operators/type_conversion_functions
       Comparison
      functions 5_searching/expressions,_functions,_and_operators/comparison_functions
       Miscellaneous
      functions 5_searching/expressions,_functions,_and_operators/miscellaneous_functions

    Sorting modes 5_searching/sorting_modes
    Grouping (clustering) search
   results 5_searching/grouping_clustering_search_results
    Distributed searching 5_searching/distributed_searching
    searchd query log
   formats 5_searching/searchd_query_log_formats/README.9

       Plain log
      format 5_searching/searchd_query_log_formats/plain_log_format
       SphinxQL log
      format 5_searching/searchd_query_log_formats/sphinxql_log_format

    MySQL protocol support and
   SphinxQL 5_searching/mysql_protocol_support_and_sphinxql
    HTTP protocol 5_searching/http_protocol
    Multi-queries 5_searching/multi-queries
    Collations 5_searching/collations
    Query cache 5_searching/query_cache
    6. Extending Sphinx 6_extending_sphinx/README
    Sphinx UDFs (User Defined
   Functions) 6_extending_sphinx/sphinx_udfs_user_defined_functions
    Sphinx plugins 6_extending_sphinx/sphinx_plugins
    Ranker plugins 6_extending_sphinx/ranker_plugins
    7. Command line tools
   reference 7_command_line_tools_reference/README
    indexer command
   reference 7_command_line_tools_reference/indexer_command_reference
    searchd command
   reference 7_command_line_tools_reference/searchd_command_reference
    spelldump command
   reference 7_command_line_tools_reference/spelldump_command_reference
    indextool command
   reference 7_command_line_tools_reference/indextool_command_reference
    wordbreaker command
   reference 7_command_line_tools_reference/wordbreaker_command_reference
    8. SphinxQL reference 8_sphinxql_reference/README
    SELECT syntax 8_sphinxql_reference/select_syntax
-  [SELECT @@system\_variable
   syntax](8\_sphinxql\_reference/select\_systemvariable\_syntax)
    SHOW META syntax 8_sphinxql_reference/show_meta_syntax
    SHOW WARNINGS
   syntax 8_sphinxql_reference/show_warnings_syntax
    SHOW STATUS syntax 8_sphinxql_reference/show_status_syntax
    INSERT and REPLACE
   syntax 8_sphinxql_reference/insert_and_replace_syntax
    REPLACE syntax 8_sphinxql_reference/replace_syntax
    DELETE syntax 8_sphinxql_reference/delete_syntax
    SET syntax 8_sphinxql_reference/set_syntax
    SET TRANSACTION
   syntax 8_sphinxql_reference/set_transaction_syntax
    BEGIN, COMMIT, and ROLLBACK
   syntax 8_sphinxql_reference/begin,_commit,_and_rollback_syntax
    BEGIN syntax 8_sphinxql_reference/begin_syntax
    ROLLBACK syntax 8_sphinxql_reference/rollback_syntax
    CALL SNIPPETS
   syntax 8_sphinxql_reference/call_snippets_syntax
    CALL KEYWORDS
   syntax 8_sphinxql_reference/call_keywords_syntax
    CALL QSUGGEST
   syntax 8_sphinxql_reference/call_qsuggest_syntax
    CALL SUGGEST syntax 8_sphinxql_reference/call_suggest_syntax
    SHOW TABLES syntax 8_sphinxql_reference/show_tables_syntax
    DESCRIBE syntax 8_sphinxql_reference/describe_syntax
    CREATE FUNCTION
   syntax 8_sphinxql_reference/create_function_syntax
    DROP FUNCTION
   syntax 8_sphinxql_reference/drop_function_syntax
    SHOW VARIABLES
   syntax 8_sphinxql_reference/show_variables_syntax
    SHOW COLLATION
   syntax 8_sphinxql_reference/show_collation_syntax
    SHOW CHARACTER SET
   syntax 8_sphinxql_reference/show_character_set_syntax
    UPDATE syntax 8_sphinxql_reference/update_syntax
    ALTER syntax 8_sphinxql_reference/alter_syntax
    ATTACH INDEX syntax 8_sphinxql_reference/attach_index_syntax
    FLUSH RTINDEX
   syntax 8_sphinxql_reference/flush_rtindex_syntax
    FLUSH RAMCHUNK
   syntax 8_sphinxql_reference/flush_ramchunk_syntax
    FLUSH ATTRIBUTES
   syntax 8_sphinxql_reference/flush_attributes_syntax
    FLUSH HOSTNAMES
   syntax 8_sphinxql_reference/flush_hostnames_syntax
    TRUNCATE RTINDEX
   syntax 8_sphinxql_reference/truncate_rtindex_syntax
    SHOW AGENT STATUS 8_sphinxql_reference/show_agent_status
    SHOW PROFILE syntax 8_sphinxql_reference/show_profile_syntax
    SHOW INDEX STATUS
   syntax 8_sphinxql_reference/show_index_status_syntax
    SHOW INDEX SETTINGS
   syntax 8_sphinxql_reference/show_index_settings_syntax
    OPTIMIZE INDEX
   syntax 8_sphinxql_reference/optimize_index_syntax
    SHOW PLAN syntax 8_sphinxql_reference/show_plan_syntax
    SHOW DATABASES
   syntax 8_sphinxql_reference/show_databases_syntax
    CREATE PLUGIN
   syntax 8_sphinxql_reference/create_plugin_syntax
    DROP PLUGIN syntax 8_sphinxql_reference/drop_plugin_syntax
    SHOW PLUGINS syntax 8_sphinxql_reference/show_plugins_syntax
    RELOAD PLUGINS
   syntax 8_sphinxql_reference/reload_plugins_syntax
    SHOW THREADS syntax 8_sphinxql_reference/show_threads_syntax
    RELOAD INDEX syntax 8_sphinxql_reference/reload_index_syntax
    Multi-statement
   queries 8_sphinxql_reference/multi-statement_queries
    Comment syntax 8_sphinxql_reference/comment_syntax
    List of SphinxQL reserved
   keywords 8_sphinxql_reference/list_of_sphinxql_reserved_keywords
    9. API reference 9_api_reference/README
    General API
   functions 9_api_reference/general_api_functions/README

       GetLastError 9_api_reference/general_api_functions/getlasterror
       GetLastWarning 9_api_reference/general_api_functions/getlastwarning
       SetServer 9_api_reference/general_api_functions/setserver
       SetRetries 9_api_reference/general_api_functions/setretries
       SetConnectTimeout 9_api_reference/general_api_functions/setconnecttimeout
       SetArrayResult 9_api_reference/general_api_functions/setarrayresult
       IsConnectError 9_api_reference/general_api_functions/isconnecterror

    General query
   settings 9_api_reference/general_query_settings/README.2

       SetLimits 9_api_reference/general_query_settings/setlimits
       SetMaxQueryTime 9_api_reference/general_query_settings/setmaxquerytime
       SetOverride 9_api_reference/general_query_settings/setoverride
       SetSelect 9_api_reference/general_query_settings/setselect

    Full-text search query
   settings 9_api_reference/full-text_search_query_settings/README.3

       SetMatchMode 9_api_reference/full-text_search_query_settings/setmatchmode
       SetRankingMode 9_api_reference/full-text_search_query_settings/setrankingmode
       SetSortMode 9_api_reference/full-text_search_query_settings/setsortmode
       SetWeights 9_api_reference/full-text_search_query_settings/setweights
       SetFieldWeights 9_api_reference/full-text_search_query_settings/setfieldweights
       SetIndexWeights 9_api_reference/full-text_search_query_settings/setindexweights

    Result set filtering
   settings 9_api_reference/result_set_filtering_settings/README.4

       SetIDRange 9_api_reference/result_set_filtering_settings/setidrange
       SetFilter 9_api_reference/result_set_filtering_settings/setfilter
       SetFilterRange 9_api_reference/result_set_filtering_settings/setfilterrange
       SetFilterFloatRange 9_api_reference/result_set_filtering_settings/setfilterfloatrange
       SetGeoAnchor 9_api_reference/result_set_filtering_settings/setgeoanchor
       SetFilterString 9_api_reference/result_set_filtering_settings/setfilterstring

    GROUP BY settings 9_api_reference/group_by_settings/README.5

       SetGroupBy 9_api_reference/group_by_settings/setgroupby
       SetGroupDistinct 9_api_reference/group_by_settings/setgroupdistinct

    Querying 9_api_reference/querying/README.6

       Query 9_api_reference/querying/query
       AddQuery 9_api_reference/querying/addquery
       RunQueries 9_api_reference/querying/runqueries
       ResetFilters 9_api_reference/querying/resetfilters
       ResetGroupBy 9_api_reference/querying/resetgroupby

    Additional
   functionality 9_api_reference/additional_functionality/README.7

       BuildExcerpts 9_api_reference/additional_functionality/buildexcerpts
       UpdateAttributes 9_api_reference/additional_functionality/updateattributes
       BuildKeywords 9_api_reference/additional_functionality/buildkeywords
       EscapeString 9_api_reference/additional_functionality/escapestring
       Status 9_api_reference/additional_functionality/status
       FlushAttributes 9_api_reference/additional_functionality/flushattributes

    Persistent
   connections 9_api_reference/persistent_connections/README.8

       Open 9_api_reference/persistent_connections/open
       Close 9_api_reference/persistent_connections/close

    10. MySQL storage engine
   (SphinxSE) 10_mysql_storage_engine_sphinxse/README
    SphinxSE
   overview 10_mysql_storage_engine_sphinxse/sphinxse_overview
    Installing
   SphinxSE 10_mysql_storage_engine_sphinxse/installing_sphinxse/README

       Compiling MySQL 5.0.x with
      SphinxSE 10_mysql_storage_engine_sphinxse/installing_sphinxse/compiling_mysql_50x_with_sphinxse
       Compiling MySQL 5.1.x with
      SphinxSE 10_mysql_storage_engine_sphinxse/installing_sphinxse/compiling_mysql_51x_with_sphinxse
       Checking SphinxSE
      installation 10_mysql_storage_engine_sphinxse/installing_sphinxse/checking_sphinxse_installation

    Using
   SphinxSE 10_mysql_storage_engine_sphinxse/using_sphinxse
    Building snippets (excerpts) via
   MySQL 10_mysql_storage_engine_sphinxse/building_snippets_excerpts_via_mysql
    11. Reporting bugs 11_reporting_bugs
    12. sphinx.conf options
   reference 12_sphinxconf_options_reference/README
    Data source configuration
   options 12_sphinxconf_options_reference/data_source_configuration_options/README

       type 12_sphinxconf_options_reference/data_source_configuration_options/type
       sql\_host 12_sphinxconf_options_reference/data_source_configuration_options/sqlhost
       sql\_port 12_sphinxconf_options_reference/data_source_configuration_options/sqlport
       sql\_user 12_sphinxconf_options_reference/data_source_configuration_options/sqluser
       sql\_pass 12_sphinxconf_options_reference/data_source_configuration_options/sqlpass
       sql\_db 12_sphinxconf_options_reference/data_source_configuration_options/sqldb
       sql\_sock 12_sphinxconf_options_reference/data_source_configuration_options/sqlsock
       mysql\_connect\_flags 12_sphinxconf_options_reference/data_source_configuration_options/mysqlconnect_flags
       mysql\_ssl\_cert, mysql\_ssl\_key,
      mysql\_ssl\_ca 12_sphinxconf_options_reference/data_source_configuration_options/mysqlssl_cert_,_mysqlssl_key_,_mysqlssl_ca
       odbc\_dsn 12_sphinxconf_options_reference/data_source_configuration_options/odbcdsn
       sql\_query\_pre 12_sphinxconf_options_reference/data_source_configuration_options/sqlquery_pre
       sql\_query 12_sphinxconf_options_reference/data_source_configuration_options/sqlquery
       sql\_joined\_field 12_sphinxconf_options_reference/data_source_configuration_options/sqljoined_field
       sql\_query\_range 12_sphinxconf_options_reference/data_source_configuration_options/sqlquery_range
       sql\_range\_step 12_sphinxconf_options_reference/data_source_configuration_options/sqlrange_step
       sql\_query\_killlist 12_sphinxconf_options_reference/data_source_configuration_options/sqlquery_killlist
       sql\_attr\_uint 12_sphinxconf_options_reference/data_source_configuration_options/sqlattr_uint
       sql\_attr\_bool 12_sphinxconf_options_reference/data_source_configuration_options/sqlattr_bool
       sql\_attr\_bigint 12_sphinxconf_options_reference/data_source_configuration_options/sqlattr_bigint
       sql\_attr\_timestamp 12_sphinxconf_options_reference/data_source_configuration_options/sqlattr_timestamp
       sql\_attr\_float 12_sphinxconf_options_reference/data_source_configuration_options/sqlattr_float
       sql\_attr\_multi 12_sphinxconf_options_reference/data_source_configuration_options/sqlattr_multi
       sql\_attr\_string 12_sphinxconf_options_reference/data_source_configuration_options/sqlattr_string
       sql\_attr\_json 12_sphinxconf_options_reference/data_source_configuration_options/sqlattr_json
       sql\_column\_buffers 12_sphinxconf_options_reference/data_source_configuration_options/sqlcolumn_buffers
       sql\_field\_string 12_sphinxconf_options_reference/data_source_configuration_options/sqlfield_string
       sql\_file\_field 12_sphinxconf_options_reference/data_source_configuration_options/sqlfile_field
       sql\_query\_post 12_sphinxconf_options_reference/data_source_configuration_options/sqlquery_post
       sql\_query\_post\_index 12_sphinxconf_options_reference/data_source_configuration_options/sqlquery_post_index
       sql\_ranged\_throttle 12_sphinxconf_options_reference/data_source_configuration_options/sqlranged_throttle
       xmlpipe\_command 12_sphinxconf_options_reference/data_source_configuration_options/xmlpipecommand
       xmlpipe\_field 12_sphinxconf_options_reference/data_source_configuration_options/xmlpipefield
       xmlpipe\_field\_string 12_sphinxconf_options_reference/data_source_configuration_options/xmlpipefield_string
       xmlpipe\_attr\_uint 12_sphinxconf_options_reference/data_source_configuration_options/xmlpipeattr_uint
       xmlpipe\_attr\_bigint 12_sphinxconf_options_reference/data_source_configuration_options/xmlpipeattr_bigint
       xmlpipe\_attr\_bool 12_sphinxconf_options_reference/data_source_configuration_options/xmlpipeattr_bool
       xmlpipe\_attr\_timestamp 12_sphinxconf_options_reference/data_source_configuration_options/xmlpipeattr_timestamp
       xmlpipe\_attr\_float 12_sphinxconf_options_reference/data_source_configuration_options/xmlpipeattr_float
       xmlpipe\_attr\_multi 12_sphinxconf_options_reference/data_source_configuration_options/xmlpipeattr_multi
       xmlpipe\_attr\_multi\_64 12_sphinxconf_options_reference/data_source_configuration_options/xmlpipeattr_multi_64
       xmlpipe\_attr\_string 12_sphinxconf_options_reference/data_source_configuration_options/xmlpipeattr_string
       xmlpipe\_attr\_json 12_sphinxconf_options_reference/data_source_configuration_options/xmlpipeattr_json
       xmlpipe\_fixup\_utf8 12_sphinxconf_options_reference/data_source_configuration_options/xmlpipefixup_utf8
       mssql\_winauth 12_sphinxconf_options_reference/data_source_configuration_options/mssqlwinauth
       unpack\_zlib 12_sphinxconf_options_reference/data_source_configuration_options/unpackzlib
       unpack\_mysqlcompress 12_sphinxconf_options_reference/data_source_configuration_options/unpackmysqlcompress
       unpack\_mysqlcompress\_maxsize 12_sphinxconf_options_reference/data_source_configuration_options/unpackmysqlcompressmaxsize
       csvpipe\_delimiter 12_sphinxconf_options_reference/data_source_configuration_options/csvpipedelimiter

    Index configuration
   options 12_sphinxconf_options_reference/index_configuration_options/README.2

       type 12_sphinxconf_options_reference/index_configuration_options/type
       source 12_sphinxconf_options_reference/index_configuration_options/source
       path 12_sphinxconf_options_reference/index_configuration_options/path
       docinfo 12_sphinxconf_options_reference/index_configuration_options/docinfo
       mlock 12_sphinxconf_options_reference/index_configuration_options/mlock
       morphology 12_sphinxconf_options_reference/index_configuration_options/morphology
       dict 12_sphinxconf_options_reference/index_configuration_options/dict
       index\_sp 12_sphinxconf_options_reference/index_configuration_options/indexsp
       index\_zones 12_sphinxconf_options_reference/index_configuration_options/indexzones
       min\_stemming\_len 12_sphinxconf_options_reference/index_configuration_options/minstemming_len
       stopwords 12_sphinxconf_options_reference/index_configuration_options/stopwords
       wordforms 12_sphinxconf_options_reference/index_configuration_options/wordforms
       embedded\_limit 12_sphinxconf_options_reference/index_configuration_options/embeddedlimit
       exceptions 12_sphinxconf_options_reference/index_configuration_options/exceptions
       min\_word\_len 12_sphinxconf_options_reference/index_configuration_options/minword_len
       charset\_table 12_sphinxconf_options_reference/index_configuration_options/charsettable
       ignore\_chars 12_sphinxconf_options_reference/index_configuration_options/ignorechars
       min\_prefix\_len 12_sphinxconf_options_reference/index_configuration_options/minprefix_len
       min\_infix\_len 12_sphinxconf_options_reference/index_configuration_options/mininfix_len
       max\_substring\_len 12_sphinxconf_options_reference/index_configuration_options/maxsubstring_len
       prefix\_fields 12_sphinxconf_options_reference/index_configuration_options/prefixfields
       infix\_fields 12_sphinxconf_options_reference/index_configuration_options/infixfields
       ngram\_len 12_sphinxconf_options_reference/index_configuration_options/ngramlen
       ngram\_chars 12_sphinxconf_options_reference/index_configuration_options/ngramchars
       phrase\_boundary 12_sphinxconf_options_reference/index_configuration_options/phraseboundary
       phrase\_boundary\_step 12_sphinxconf_options_reference/index_configuration_options/phraseboundary_step
       html\_strip 12_sphinxconf_options_reference/index_configuration_options/htmlstrip
       html\_index\_attrs 12_sphinxconf_options_reference/index_configuration_options/htmlindex_attrs
       html\_remove\_elements 12_sphinxconf_options_reference/index_configuration_options/htmlremove_elements
       local 12_sphinxconf_options_reference/index_configuration_options/local
       agent 12_sphinxconf_options_reference/index_configuration_options/agent
       agent\_persistent 12_sphinxconf_options_reference/index_configuration_options/agentpersistent
       agent\_blackhole 12_sphinxconf_options_reference/index_configuration_options/agentblackhole
       agent\_connect\_timeout 12_sphinxconf_options_reference/index_configuration_options/agentconnect_timeout
       agent\_query\_timeout 12_sphinxconf_options_reference/index_configuration_options/agentquery_timeout
       preopen 12_sphinxconf_options_reference/index_configuration_options/preopen
       inplace\_enable 12_sphinxconf_options_reference/index_configuration_options/inplaceenable
       inplace\_hit\_gap 12_sphinxconf_options_reference/index_configuration_options/inplacehit_gap
       inplace\_docinfo\_gap 12_sphinxconf_options_reference/index_configuration_options/inplacedocinfo_gap
       inplace\_reloc\_factor 12_sphinxconf_options_reference/index_configuration_options/inplacereloc_factor
       inplace\_write\_factor 12_sphinxconf_options_reference/index_configuration_options/inplacewrite_factor
       index\_exact\_words 12_sphinxconf_options_reference/index_configuration_options/indexexact_words
       overshort\_step 12_sphinxconf_options_reference/index_configuration_options/overshortstep
       stopword\_step 12_sphinxconf_options_reference/index_configuration_options/stopwordstep
       hitless\_words 12_sphinxconf_options_reference/index_configuration_options/hitlesswords
       expand\_keywords 12_sphinxconf_options_reference/index_configuration_options/expandkeywords
       blend\_chars 12_sphinxconf_options_reference/index_configuration_options/blendchars
       blend\_mode 12_sphinxconf_options_reference/index_configuration_options/blendmode
       rt\_mem\_limit 12_sphinxconf_options_reference/index_configuration_options/rtmem_limit
       rt\_field 12_sphinxconf_options_reference/index_configuration_options/rtfield
       rt\_attr\_uint 12_sphinxconf_options_reference/index_configuration_options/rtattr_uint
       rt\_attr\_bool 12_sphinxconf_options_reference/index_configuration_options/rtattr_bool
       rt\_attr\_bigint 12_sphinxconf_options_reference/index_configuration_options/rtattr_bigint
       rt\_attr\_float 12_sphinxconf_options_reference/index_configuration_options/rtattr_float
       rt\_attr\_multi 12_sphinxconf_options_reference/index_configuration_options/rtattr_multi
       rt\_attr\_multi\_64 12_sphinxconf_options_reference/index_configuration_options/rtattr_multi_64
       rt\_attr\_timestamp 12_sphinxconf_options_reference/index_configuration_options/rtattr_timestamp
       rt\_attr\_string 12_sphinxconf_options_reference/index_configuration_options/rtattr_string
       rt\_attr\_json 12_sphinxconf_options_reference/index_configuration_options/rtattr_json
       ha\_strategy 12_sphinxconf_options_reference/index_configuration_options/hastrategy
       bigram\_freq\_words 12_sphinxconf_options_reference/index_configuration_options/bigramfreq_words
       bigram\_index 12_sphinxconf_options_reference/index_configuration_options/bigramindex
       index\_field\_lengths 12_sphinxconf_options_reference/index_configuration_options/indexfield_lengths
       regexp\_filter 12_sphinxconf_options_reference/index_configuration_options/regexpfilter
       stopwords\_unstemmed 12_sphinxconf_options_reference/index_configuration_options/stopwordsunstemmed
       global\_idf 12_sphinxconf_options_reference/index_configuration_options/globalidf
       rlp\_context 12_sphinxconf_options_reference/index_configuration_options/rlpcontext
       ondisk\_attrs 12_sphinxconf_options_reference/index_configuration_options/ondiskattrs

    indexer program configuration
   options 12_sphinxconf_options_reference/indexer_program_configuration_options/README.3

       mem\_limit 12_sphinxconf_options_reference/indexer_program_configuration_options/memlimit
       max\_iops 12_sphinxconf_options_reference/indexer_program_configuration_options/maxiops
       max\_iosize 12_sphinxconf_options_reference/indexer_program_configuration_options/maxiosize
       max\_xmlpipe2\_field 12_sphinxconf_options_reference/indexer_program_configuration_options/maxxmlpipe2_field
       write\_buffer 12_sphinxconf_options_reference/indexer_program_configuration_options/writebuffer
       max\_file\_field\_buffer 12_sphinxconf_options_reference/indexer_program_configuration_options/maxfile_field_buffer
       on\_file\_field\_error 12_sphinxconf_options_reference/indexer_program_configuration_options/onfile_field_error
       lemmatizer\_cache 12_sphinxconf_options_reference/indexer_program_configuration_options/lemmatizercache

    searchd program configuration
   options 12_sphinxconf_options_reference/searchd_program_configuration_options/README.4

       listen 12_sphinxconf_options_reference/searchd_program_configuration_options/listen
       log 12_sphinxconf_options_reference/searchd_program_configuration_options/log
       query\_log 12_sphinxconf_options_reference/searchd_program_configuration_options/querylog
       query\_log\_format 12_sphinxconf_options_reference/searchd_program_configuration_options/querylog_format
       read\_timeout 12_sphinxconf_options_reference/searchd_program_configuration_options/readtimeout
       client\_timeout 12_sphinxconf_options_reference/searchd_program_configuration_options/clienttimeout
       sphinxql\_timeout 12_sphinxconf_options_reference/searchd_program_configuration_options/sphinxqltimeout
       max\_children 12_sphinxconf_options_reference/searchd_program_configuration_options/maxchildren
       net\_workers 12_sphinxconf_options_reference/searchd_program_configuration_options/networkers
       queue\_max\_length 12_sphinxconf_options_reference/searchd_program_configuration_options/queuemax_length
       pid\_file 12_sphinxconf_options_reference/searchd_program_configuration_options/pidfile
       seamless\_rotate 12_sphinxconf_options_reference/searchd_program_configuration_options/seamlessrotate
       preopen\_indexes 12_sphinxconf_options_reference/searchd_program_configuration_options/preopenindexes
       unlink\_old 12_sphinxconf_options_reference/searchd_program_configuration_options/unlinkold
       attr\_flush\_period 12_sphinxconf_options_reference/searchd_program_configuration_options/attrflush_period
       max\_packet\_size 12_sphinxconf_options_reference/searchd_program_configuration_options/maxpacket_size
       mva\_updates\_pool 12_sphinxconf_options_reference/searchd_program_configuration_options/mvaupdates_pool
       max\_filters 12_sphinxconf_options_reference/searchd_program_configuration_options/maxfilters
       max\_filter\_values 12_sphinxconf_options_reference/searchd_program_configuration_options/maxfilter_values
       listen\_backlog 12_sphinxconf_options_reference/searchd_program_configuration_options/listenbacklog
       read\_buffer 12_sphinxconf_options_reference/searchd_program_configuration_options/readbuffer
       read\_unhinted 12_sphinxconf_options_reference/searchd_program_configuration_options/readunhinted
       max\_batch\_queries 12_sphinxconf_options_reference/searchd_program_configuration_options/maxbatch_queries
       subtree\_docs\_cache 12_sphinxconf_options_reference/searchd_program_configuration_options/subtreedocs_cache
       subtree\_hits\_cache 12_sphinxconf_options_reference/searchd_program_configuration_options/subtreehits_cache
       workers 12_sphinxconf_options_reference/searchd_program_configuration_options/workers
       dist\_threads 12_sphinxconf_options_reference/searchd_program_configuration_options/distthreads
       binlog\_path 12_sphinxconf_options_reference/searchd_program_configuration_options/binlogpath
       binlog\_flush 12_sphinxconf_options_reference/searchd_program_configuration_options/binlogflush
       binlog\_max\_log\_size 12_sphinxconf_options_reference/searchd_program_configuration_options/binlogmax_log_size
       snippets\_file\_prefix 12_sphinxconf_options_reference/searchd_program_configuration_options/snippetsfile_prefix
       collation\_server 12_sphinxconf_options_reference/searchd_program_configuration_options/collationserver
       collation\_libc\_locale 12_sphinxconf_options_reference/searchd_program_configuration_options/collationlibc_locale
       mysql\_version\_string 12_sphinxconf_options_reference/searchd_program_configuration_options/mysqlversion_string
       rt\_flush\_period 12_sphinxconf_options_reference/searchd_program_configuration_options/rtflush_period
       thread\_stack 12_sphinxconf_options_reference/searchd_program_configuration_options/threadstack
       expansion\_limit 12_sphinxconf_options_reference/searchd_program_configuration_options/expansionlimit
       watchdog 12_sphinxconf_options_reference/searchd_program_configuration_options/watchdog
       sphinxql\_state 12_sphinxconf_options_reference/searchd_program_configuration_options/sphinxqlstate
       ha\_ping\_interval 12_sphinxconf_options_reference/searchd_program_configuration_options/haping_interval
       ha\_period\_karma 12_sphinxconf_options_reference/searchd_program_configuration_options/haperiod_karma
       persistent\_connections\_limit 12_sphinxconf_options_reference/searchd_program_configuration_options/persistentconnections_limit
       rt\_merge\_iops 12_sphinxconf_options_reference/searchd_program_configuration_options/rtmerge_iops
       rt\_merge\_maxiosize 12_sphinxconf_options_reference/searchd_program_configuration_options/rtmerge_maxiosize
       predicted\_time\_costs 12_sphinxconf_options_reference/searchd_program_configuration_options/predictedtime_costs
       shutdown\_timeout 12_sphinxconf_options_reference/searchd_program_configuration_options/shutdowntimeout
       ondisk\_attrs\_default 12_sphinxconf_options_reference/searchd_program_configuration_options/ondiskattrs_default
       query\_log\_min\_msec 12_sphinxconf_options_reference/searchd_program_configuration_options/querylog_min_msec
       agent\_connect\_timeout 12_sphinxconf_options_reference/searchd_program_configuration_options/agentconnect_timeout
       agent\_query\_timeout 12_sphinxconf_options_reference/searchd_program_configuration_options/agentquery_timeout
       agent\_retry\_count 12_sphinxconf_options_reference/searchd_program_configuration_options/agentretry_count
       agent\_retry\_delay 12_sphinxconf_options_reference/searchd_program_configuration_options/agentretry_delay
       hostname\_lookup 12_sphinxconf_options_reference/searchd_program_configuration_options/hostnamelookup
       qcache\_max\_bytes 12_sphinxconf_options_reference/searchd_program_configuration_options/qcachemax_bytes
       qcache\_thresh\_msec 12_sphinxconf_options_reference/searchd_program_configuration_options/qcachethresh_msec
       qcache\_ttl\_sec 12_sphinxconf_options_reference/searchd_program_configuration_options/qcachettl_sec
       grouping\_in\_utc 12_sphinxconf_options_reference/searchd_program_configuration_options/groupingin_utc

    Common section configuration
   options 12_sphinxconf_options_reference/common_section_configuration_options/README.5

       lemmatizer\_base 12_sphinxconf_options_reference/common_section_configuration_options/lemmatizerbase
       on\_json\_attr\_error 12_sphinxconf_options_reference/common_section_configuration_options/onjson_attr_error
       json\_autoconv\_numbers 12_sphinxconf_options_reference/common_section_configuration_options/jsonautoconv_numbers
       json\_autoconv\_keynames 12_sphinxconf_options_reference/common_section_configuration_options/jsonautoconv_keynames
       rlp\_root 12_sphinxconf_options_reference/common_section_configuration_options/rlproot
       rlp\_environment 12_sphinxconf_options_reference/common_section_configuration_options/rlpenvironment
       rlp\_max\_batch\_size 12_sphinxconf_options_reference/common_section_configuration_options/rlpmax_batch_size
       rlp\_max\_batch\_docs 12_sphinxconf_options_reference/common_section_configuration_options/rlpmax_batch_docs
       plugin\_dir 12_sphinxconf_options_reference/common_section_configuration_options/plugindir

    A. Sphinx revision history a_sphinx_revision_history/README
    Version 2.3.2-beta, 09 sep
   2016 a_sphinx_revision_history/version_232-beta,_09_sep_2016
    Version 2.3.1-beta, 03 mar
   2015 a_sphinx_revision_history/version_231-beta,_03_mar_2015
    Version 2.2.11-release, 19 jul
   2016 a_sphinx_revision_history/version_2211-release,_19_jul_2016
    Version 2.2.10-release, 07 sep
   2015 a_sphinx_revision_history/version_2210-release,_07_sep_2015
    Version 2.2.9-release, 16 apr
   2015 a_sphinx_revision_history/version_229-release,_16_apr_2015
    Version 2.2.8-release, 09 mar
   2015 a_sphinx_revision_history/version_228-release,_09_mar_2015
    Version 2.2.7-release, 20 jan
   2015 a_sphinx_revision_history/version_227-release,_20_jan_2015
    Version 2.2.6-release, 13 nov
   2014 a_sphinx_revision_history/version_226-release,_13_nov_2014
    Version 2.2.5-release, 06 oct
   2014 a_sphinx_revision_history/version_225-release,_06_oct_2014
    Version 2.2.4-release, 11 sep
   2014 a_sphinx_revision_history/version_224-release,_11_sep_2014
    Version 2.2.3-beta, 13 may
   2014 a_sphinx_revision_history/version_223-beta,_13_may_2014
    Version 2.2.2-beta, 11 feb
   2014 a_sphinx_revision_history/version_222-beta,_11_feb_2014
    Version 2.2.1-beta, 13 nov
   2013 a_sphinx_revision_history/version_221-beta,_13_nov_2013
    Version 2.1.9-release, 03 jul
   2014 a_sphinx_revision_history/version_219-release,_03_jul_2014
    Version 2.1.8-release, 28 apr
   2014 a_sphinx_revision_history/version_218-release,_28_apr_2014
    Version 2.1.7-release, 30 mar
   2014 a_sphinx_revision_history/version_217-release,_30_mar_2014
    Version 2.1.6-release, 24 feb
   2014 a_sphinx_revision_history/version_216-release,_24_feb_2014
    Version 2.1.5-release, 22 jan
   2014 a_sphinx_revision_history/version_215-release,_22_jan_2014
    Version 2.1.4-release, 18 dec
   2013 a_sphinx_revision_history/version_214-release,_18_dec_2013
    Version 2.1.3-release, 12 nov
   2013 a_sphinx_revision_history/version_213-release,_12_nov_2013
    Version 2.1.2-release, 10 oct
   2013 a_sphinx_revision_history/version_212-release,_10_oct_2013
    Version 2.1.1-beta, 20 feb
   2013 a_sphinx_revision_history/version_211-beta,_20_feb_2013
    Version 2.0.10-release, 22 jan
   2014 a_sphinx_revision_history/version_2010-release,_22_jan_2014
    Version 2.0.9-release, 26 aug
   2013 a_sphinx_revision_history/version_209-release,_26_aug_2013
    Version 2.0.8-release, 26 apr
   2013 a_sphinx_revision_history/version_208-release,_26_apr_2013
    Version 2.0.7-release, 26 mar
   2013 a_sphinx_revision_history/version_207-release,_26_mar_2013
    Version 2.0.6-release, 22 oct
   2012 a_sphinx_revision_history/version_206-release,_22_oct_2012
    Version 2.0.5-release, 28 jul
   2012 a_sphinx_revision_history/version_205-release,_28_jul_2012
    Version 2.0.4-release, 02 mar
   2012 a_sphinx_revision_history/version_204-release,_02_mar_2012
    Version 2.0.3-release, 23 dec
   2011 a_sphinx_revision_history/version_203-release,_23_dec_2011
    Version 2.0.2-beta, 15 nov
   2011 a_sphinx_revision_history/version_202-beta,_15_nov_2011
    Version 2.0.1-beta, 22 apr
   2011 a_sphinx_revision_history/version_201-beta,_22_apr_2011
    Version 1.10-beta, 19 jul
   2010 a_sphinx_revision_history/version_110-beta,_19_jul_2010
    Version 0.9.9-release, 02 dec
   2009 a_sphinx_revision_history/version_099-release,_02_dec_2009
    Version 0.9.9-rc2, 08 apr
   2009 a_sphinx_revision_history/version_099-rc2,_08_apr_2009
    Version 0.9.9-rc1, 17 nov
   2008 a_sphinx_revision_history/version_099-rc1,_17_nov_2008
    Version 0.9.8.1, 30 oct
   2008 a_sphinx_revision_history/version_0981,_30_oct_2008
    Version 0.9.8, 14 jul
   2008 a_sphinx_revision_history/version_098,_14_jul_2008
    Version 0.9.7, 02 apr
   2007 a_sphinx_revision_history/version_097,_02_apr_2007
    Version 0.9.7-rc2, 15 dec
   2006 a_sphinx_revision_history/version_097-rc2,_15_dec_2006
    Version 0.9.7-rc1, 26 oct
   2006 a_sphinx_revision_history/version_097-rc1,_26_oct_2006
    Version 0.9.6, 24 jul
   2006 a_sphinx_revision_history/version_096,_24_jul_2006
    Version 0.9.6-rc1, 26 jun
   2006 a_sphinx_revision_history/version_096-rc1,_26_jun_2006
    About about
    Sphinx features sphinx_features
    Where to get Sphinx where_to_get_sphinx
    License license
    Credits credits
    History history
    Supported systems supported_systems
    Compiling Sphinx from
   source compiling_sphinx_from_source/README
    Required tools compiling_sphinx_from_source/required_tools
    Compiling on
   Linux compiling_sphinx_from_source/compiling_on_linux
    Known compilation
   issues compiling_sphinx_from_source/known_compilation_issues
    Installing Sphinx packages on Debian and
   Ubuntu installing_sphinx_packages_on_debian_and_ubuntu
    Installing Sphinx packages on RedHat and
   CentOS installing_sphinx_packages_on_redhat_and_centos
    Installing Sphinx on Windows installing_sphinx_on_windows
    Sphinx deprecations and changes in default
   configuration sphinx_deprecations_and_changes_in_default_configu
    Quick Sphinx usage tour quick_sphinx_usage_tour
    Data sources data_sources
    Full-text fields full-text_fields
    Attributes attributes
    MVA (multi-valued attributes) mva_multi-valued_attributes
    Indexes indexes
    Restrictions on the source
   data restrictions_on_the_source_data
    Charsets, case folding, translation tables, and replacement
   rules charsets,_case_folding,_translation_tables,_and_re
    SQL data sources (MySQL,
   PostgreSQL) sql_data_sources_mysql,_postgresql
    xmlpipe2 data source xmlpipe2_data_source
    tsvpipe:raw-latex:`\csvpipe `(Tab:raw-latex:`\Comma `Separated
   Values) data
   source tsvpipecsvpipe_tabcomma_separated_values_data_sour
    Live index updates live_index_updates
    Delta index updates delta_index_updates
    Index merging index_merging
    RT indexes overview rt_indexes_overview
    Known caveats with RT indexes known_caveats_with_rt_indexes
    RT index internals rt_index_internals
    Binary logging binary_logging
    Matching modes matching_modes
    Boolean query syntax boolean_query_syntax
    Extended query syntax extended_query_syntax
    Search results ranking search_results_ranking/README
    Ranking overview search_results_ranking/ranking_overview
    Available built-in
   rankers search_results_ranking/available_built-in_rankers
    Expression based ranker
   (SPH\_RANK\_EXPR) search_results_ranking/expression_based_ranker_sphrank_expr
    Quick summary of the ranking
   factors search_results_ranking/quick_summary_of_the_ranking_factors
    Document-level ranking
   factors search_results_ranking/document-level_ranking_factors
    Field-level ranking
   factors search_results_ranking/field-level_ranking_factors
    Ranking factor aggregation
   functions search_results_ranking/ranking_factor_aggregation_functions
    Formula expressions for all the built-in
   rankers search_results_ranking/formula_expressions_for_all_the_built-in_rankers
    Expressions, functions, and
   operators expressions,_functions,_and_operators/README
    Operators expressions,_functions,_and_operators/operators
    Numeric
   functions expressions,_functions,_and_operators/numeric_functions
    Date and time
   functions expressions,_functions,_and_operators/date_and_time_functions
    Type conversion
   functions expressions,_functions,_and_operators/type_conversion_functions
    Comparison
   functions expressions,_functions,_and_operators/comparison_functions
    Miscellaneous
   functions expressions,_functions,_and_operators/miscellaneous_functions
    Sorting modes sorting_modes
    Grouping (clustering) search
   results grouping_clustering_search_results
    Distributed searching distributed_searching
    searchd query log formats searchd_query_log_formats/README
    Plain log format searchd_query_log_formats/plain_log_format
    SphinxQL log
   format searchd_query_log_formats/sphinxql_log_format
    MySQL protocol support and
   SphinxQL mysql_protocol_support_and_sphinxql
    HTTP protocol http_protocol
    Multi-queries multi-queries
    Collations collations
    Query cache query_cache
    Sphinx UDFs (User Defined
   Functions) sphinx_udfs_user_defined_functions
    Sphinx plugins sphinx_plugins
    Ranker plugins ranker_plugins
    indexer command reference indexer_command_reference
    searchd command reference searchd_command_reference
    spelldump command reference spelldump_command_reference
    indextool command reference indextool_command_reference
    wordbreaker command reference wordbreaker_command_reference
    SELECT syntax select_syntax
-  [SELECT @@system\_variable syntax](select\_systemvariable\_syntax)
    SHOW META syntax show_meta_syntax
    SHOW WARNINGS syntax show_warnings_syntax
    SHOW STATUS syntax show_status_syntax
    INSERT and REPLACE syntax insert_and_replace_syntax
    REPLACE syntax replace_syntax
    DELETE syntax delete_syntax
    SET syntax set_syntax
    SET TRANSACTION syntax set_transaction_syntax
    BEGIN, COMMIT, and ROLLBACK
   syntax begin,_commit,_and_rollback_syntax
    BEGIN syntax begin_syntax
    ROLLBACK syntax rollback_syntax
    CALL SNIPPETS syntax call_snippets_syntax
    CALL KEYWORDS syntax call_keywords_syntax
    CALL QSUGGEST syntax call_qsuggest_syntax
    CALL SUGGEST syntax call_suggest_syntax
    SHOW TABLES syntax show_tables_syntax
    DESCRIBE syntax describe_syntax
    CREATE FUNCTION syntax create_function_syntax
    DROP FUNCTION syntax drop_function_syntax
    SHOW VARIABLES syntax show_variables_syntax
    SHOW COLLATION syntax show_collation_syntax
    SHOW CHARACTER SET syntax show_character_set_syntax
    UPDATE syntax update_syntax
    ALTER syntax alter_syntax
    ATTACH INDEX syntax attach_index_syntax
    FLUSH RTINDEX syntax flush_rtindex_syntax
    FLUSH RAMCHUNK syntax flush_ramchunk_syntax
    FLUSH ATTRIBUTES syntax flush_attributes_syntax
    FLUSH HOSTNAMES syntax flush_hostnames_syntax
    TRUNCATE RTINDEX syntax truncate_rtindex_syntax
    SHOW AGENT STATUS show_agent_status
    SHOW PROFILE syntax show_profile_syntax
    SHOW INDEX STATUS syntax show_index_status_syntax
    SHOW INDEX SETTINGS syntax show_index_settings_syntax
    OPTIMIZE INDEX syntax optimize_index_syntax
    SHOW PLAN syntax show_plan_syntax
    SHOW DATABASES syntax show_databases_syntax
    CREATE PLUGIN syntax create_plugin_syntax
    DROP PLUGIN syntax drop_plugin_syntax
    SHOW PLUGINS syntax show_plugins_syntax
    RELOAD PLUGINS syntax reload_plugins_syntax
    SHOW THREADS syntax show_threads_syntax
    RELOAD INDEX syntax reload_index_syntax
    Multi-statement queries multi-statement_queries
    Comment syntax comment_syntax
    List of SphinxQL reserved
   keywords list_of_sphinxql_reserved_keywords
    General API functions general_api_functions/README
    GetLastError general_api_functions/getlasterror
    GetLastWarning general_api_functions/getlastwarning
    SetServer general_api_functions/setserver
    SetRetries general_api_functions/setretries
    SetConnectTimeout general_api_functions/setconnecttimeout
    SetArrayResult general_api_functions/setarrayresult
    IsConnectError general_api_functions/isconnecterror
    General query settings general_query_settings/README
    SetLimits general_query_settings/setlimits
    SetMaxQueryTime general_query_settings/setmaxquerytime
    SetOverride general_query_settings/setoverride
    SetSelect general_query_settings/setselect
    Full-text search query
   settings full-text_search_query_settings/README
    SetMatchMode full-text_search_query_settings/setmatchmode
    SetRankingMode full-text_search_query_settings/setrankingmode
    SetSortMode full-text_search_query_settings/setsortmode
    SetWeights full-text_search_query_settings/setweights
    SetFieldWeights full-text_search_query_settings/setfieldweights
    SetIndexWeights full-text_search_query_settings/setindexweights
    Result set filtering
   settings result_set_filtering_settings/README
    SetIDRange result_set_filtering_settings/setidrange
    SetFilter result_set_filtering_settings/setfilter
    SetFilterRange result_set_filtering_settings/setfilterrange
    SetFilterFloatRange result_set_filtering_settings/setfilterfloatrange
    SetGeoAnchor result_set_filtering_settings/setgeoanchor
    SetFilterString result_set_filtering_settings/setfilterstring
    GROUP BY settings group_by_settings/README
    SetGroupBy group_by_settings/setgroupby
    SetGroupDistinct group_by_settings/setgroupdistinct
    Querying querying/README
    Query querying/query
    AddQuery querying/addquery
    RunQueries querying/runqueries
    ResetFilters querying/resetfilters
    ResetGroupBy querying/resetgroupby
    Additional functionality additional_functionality/README
    BuildExcerpts additional_functionality/buildexcerpts
    UpdateAttributes additional_functionality/updateattributes
    BuildKeywords additional_functionality/buildkeywords
    EscapeString additional_functionality/escapestring
    Status additional_functionality/status
    FlushAttributes additional_functionality/flushattributes
    Persistent connections persistent_connections/README
    Open persistent_connections/open
    Close persistent_connections/close
    SphinxSE overview sphinxse_overview
    Installing SphinxSE installing_sphinxse/README
    Compiling MySQL 5.0.x with
   SphinxSE installing_sphinxse/compiling_mysql_50x_with_sphinxse
    Compiling MySQL 5.1.x with
   SphinxSE installing_sphinxse/compiling_mysql_51x_with_sphinxse
    Checking SphinxSE
   installation installing_sphinxse/checking_sphinxse_installation
    Using SphinxSE using_sphinxse
    Building snippets (excerpts) via
   MySQL building_snippets_excerpts_via_mysql
    Data source configuration
   options data_source_configuration_options/README
    type data_source_configuration_options/type
    sql\_host data_source_configuration_options/sqlhost
    sql\_port data_source_configuration_options/sqlport
    sql\_user data_source_configuration_options/sqluser
    sql\_pass data_source_configuration_options/sqlpass
    sql\_db data_source_configuration_options/sqldb
    sql\_sock data_source_configuration_options/sqlsock
    mysql\_connect\_flags data_source_configuration_options/mysqlconnect_flags
    mysql\_ssl\_cert, mysql\_ssl\_key,
   mysql\_ssl\_ca data_source_configuration_options/mysqlssl_cert_,_mysqlssl_key_,_mysqlssl_ca
    odbc\_dsn data_source_configuration_options/odbcdsn
    sql\_query\_pre data_source_configuration_options/sqlquery_pre
    sql\_query data_source_configuration_options/sqlquery
    sql\_joined\_field data_source_configuration_options/sqljoined_field
    sql\_query\_range data_source_configuration_options/sqlquery_range
    sql\_range\_step data_source_configuration_options/sqlrange_step
    sql\_query\_killlist data_source_configuration_options/sqlquery_killlist
    sql\_attr\_uint data_source_configuration_options/sqlattr_uint
    sql\_attr\_bool data_source_configuration_options/sqlattr_bool
    sql\_attr\_bigint data_source_configuration_options/sqlattr_bigint
    sql\_attr\_timestamp data_source_configuration_options/sqlattr_timestamp
    sql\_attr\_float data_source_configuration_options/sqlattr_float
    sql\_attr\_multi data_source_configuration_options/sqlattr_multi
    sql\_attr\_string data_source_configuration_options/sqlattr_string
    sql\_attr\_json data_source_configuration_options/sqlattr_json
    sql\_column\_buffers data_source_configuration_options/sqlcolumn_buffers
    sql\_field\_string data_source_configuration_options/sqlfield_string
    sql\_file\_field data_source_configuration_options/sqlfile_field
    sql\_query\_post data_source_configuration_options/sqlquery_post
    sql\_query\_post\_index data_source_configuration_options/sqlquery_post_index
    sql\_ranged\_throttle data_source_configuration_options/sqlranged_throttle
    xmlpipe\_command data_source_configuration_options/xmlpipecommand
    xmlpipe\_field data_source_configuration_options/xmlpipefield
    xmlpipe\_field\_string data_source_configuration_options/xmlpipefield_string
    xmlpipe\_attr\_uint data_source_configuration_options/xmlpipeattr_uint
    xmlpipe\_attr\_bigint data_source_configuration_options/xmlpipeattr_bigint
    xmlpipe\_attr\_bool data_source_configuration_options/xmlpipeattr_bool
    xmlpipe\_attr\_timestamp data_source_configuration_options/xmlpipeattr_timestamp
    xmlpipe\_attr\_float data_source_configuration_options/xmlpipeattr_float
    xmlpipe\_attr\_multi data_source_configuration_options/xmlpipeattr_multi
    xmlpipe\_attr\_multi\_64 data_source_configuration_options/xmlpipeattr_multi_64
    xmlpipe\_attr\_string data_source_configuration_options/xmlpipeattr_string
    xmlpipe\_attr\_json data_source_configuration_options/xmlpipeattr_json
    xmlpipe\_fixup\_utf8 data_source_configuration_options/xmlpipefixup_utf8
    mssql\_winauth data_source_configuration_options/mssqlwinauth
    unpack\_zlib data_source_configuration_options/unpackzlib
    unpack\_mysqlcompress data_source_configuration_options/unpackmysqlcompress
    unpack\_mysqlcompress\_maxsize data_source_configuration_options/unpackmysqlcompressmaxsize
    csvpipe\_delimiter data_source_configuration_options/csvpipedelimiter
    Index configuration
   options index_configuration_options/README
    type index_configuration_options/type
    source index_configuration_options/source
    path index_configuration_options/path
    docinfo index_configuration_options/docinfo
    mlock index_configuration_options/mlock
    morphology index_configuration_options/morphology
    dict index_configuration_options/dict
    index\_sp index_configuration_options/indexsp
    index\_zones index_configuration_options/indexzones
    min\_stemming\_len index_configuration_options/minstemming_len
    stopwords index_configuration_options/stopwords
    wordforms index_configuration_options/wordforms
    embedded\_limit index_configuration_options/embeddedlimit
    exceptions index_configuration_options/exceptions
    min\_word\_len index_configuration_options/minword_len
    charset\_table index_configuration_options/charsettable
    ignore\_chars index_configuration_options/ignorechars
    min\_prefix\_len index_configuration_options/minprefix_len
    min\_infix\_len index_configuration_options/mininfix_len
    max\_substring\_len index_configuration_options/maxsubstring_len
    prefix\_fields index_configuration_options/prefixfields
    infix\_fields index_configuration_options/infixfields
    ngram\_len index_configuration_options/ngramlen
    ngram\_chars index_configuration_options/ngramchars
    phrase\_boundary index_configuration_options/phraseboundary
    phrase\_boundary\_step index_configuration_options/phraseboundary_step
    html\_strip index_configuration_options/htmlstrip
    html\_index\_attrs index_configuration_options/htmlindex_attrs
    html\_remove\_elements index_configuration_options/htmlremove_elements
    local index_configuration_options/local
    agent index_configuration_options/agent
    agent\_persistent index_configuration_options/agentpersistent
    agent\_blackhole index_configuration_options/agentblackhole
    agent\_connect\_timeout index_configuration_options/agentconnect_timeout
    agent\_query\_timeout index_configuration_options/agentquery_timeout
    preopen index_configuration_options/preopen
    inplace\_enable index_configuration_options/inplaceenable
    inplace\_hit\_gap index_configuration_options/inplacehit_gap
    inplace\_docinfo\_gap index_configuration_options/inplacedocinfo_gap
    inplace\_reloc\_factor index_configuration_options/inplacereloc_factor
    inplace\_write\_factor index_configuration_options/inplacewrite_factor
    index\_exact\_words index_configuration_options/indexexact_words
    overshort\_step index_configuration_options/overshortstep
    stopword\_step index_configuration_options/stopwordstep
    hitless\_words index_configuration_options/hitlesswords
    expand\_keywords index_configuration_options/expandkeywords
    blend\_chars index_configuration_options/blendchars
    blend\_mode index_configuration_options/blendmode
    rt\_mem\_limit index_configuration_options/rtmem_limit
    rt\_field index_configuration_options/rtfield
    rt\_attr\_uint index_configuration_options/rtattr_uint
    rt\_attr\_bool index_configuration_options/rtattr_bool
    rt\_attr\_bigint index_configuration_options/rtattr_bigint
    rt\_attr\_float index_configuration_options/rtattr_float
    rt\_attr\_multi index_configuration_options/rtattr_multi
    rt\_attr\_multi\_64 index_configuration_options/rtattr_multi_64
    rt\_attr\_timestamp index_configuration_options/rtattr_timestamp
    rt\_attr\_string index_configuration_options/rtattr_string
    rt\_attr\_json index_configuration_options/rtattr_json
    ha\_strategy index_configuration_options/hastrategy
    bigram\_freq\_words index_configuration_options/bigramfreq_words
    bigram\_index index_configuration_options/bigramindex
    index\_field\_lengths index_configuration_options/indexfield_lengths
    regexp\_filter index_configuration_options/regexpfilter
    stopwords\_unstemmed index_configuration_options/stopwordsunstemmed
    global\_idf index_configuration_options/globalidf
    rlp\_context index_configuration_options/rlpcontext
    ondisk\_attrs index_configuration_options/ondiskattrs
    indexer program configuration
   options indexer_program_configuration_options/README
    mem\_limit indexer_program_configuration_options/memlimit
    max\_iops indexer_program_configuration_options/maxiops
    max\_iosize indexer_program_configuration_options/maxiosize
    max\_xmlpipe2\_field indexer_program_configuration_options/maxxmlpipe2_field
    write\_buffer indexer_program_configuration_options/writebuffer
    max\_file\_field\_buffer indexer_program_configuration_options/maxfile_field_buffer
    on\_file\_field\_error indexer_program_configuration_options/onfile_field_error
    lemmatizer\_cache indexer_program_configuration_options/lemmatizercache
    searchd program configuration
   options searchd_program_configuration_options/README
    listen searchd_program_configuration_options/listen
    log searchd_program_configuration_options/log
    query\_log searchd_program_configuration_options/querylog
    query\_log\_format searchd_program_configuration_options/querylog_format
    read\_timeout searchd_program_configuration_options/readtimeout
    client\_timeout searchd_program_configuration_options/clienttimeout
    sphinxql\_timeout searchd_program_configuration_options/sphinxqltimeout
    max\_children searchd_program_configuration_options/maxchildren
    net\_workers searchd_program_configuration_options/networkers
    queue\_max\_length searchd_program_configuration_options/queuemax_length
    pid\_file searchd_program_configuration_options/pidfile
    seamless\_rotate searchd_program_configuration_options/seamlessrotate
    preopen\_indexes searchd_program_configuration_options/preopenindexes
    unlink\_old searchd_program_configuration_options/unlinkold
    attr\_flush\_period searchd_program_configuration_options/attrflush_period
    max\_packet\_size searchd_program_configuration_options/maxpacket_size
    mva\_updates\_pool searchd_program_configuration_options/mvaupdates_pool
    max\_filters searchd_program_configuration_options/maxfilters
    max\_filter\_values searchd_program_configuration_options/maxfilter_values
    listen\_backlog searchd_program_configuration_options/listenbacklog
    read\_buffer searchd_program_configuration_options/readbuffer
    read\_unhinted searchd_program_configuration_options/readunhinted
    max\_batch\_queries searchd_program_configuration_options/maxbatch_queries
    subtree\_docs\_cache searchd_program_configuration_options/subtreedocs_cache
    subtree\_hits\_cache searchd_program_configuration_options/subtreehits_cache
    workers searchd_program_configuration_options/workers
    dist\_threads searchd_program_configuration_options/distthreads
    binlog\_path searchd_program_configuration_options/binlogpath
    binlog\_flush searchd_program_configuration_options/binlogflush
    binlog\_max\_log\_size searchd_program_configuration_options/binlogmax_log_size
    snippets\_file\_prefix searchd_program_configuration_options/snippetsfile_prefix
    collation\_server searchd_program_configuration_options/collationserver
    collation\_libc\_locale searchd_program_configuration_options/collationlibc_locale
    mysql\_version\_string searchd_program_configuration_options/mysqlversion_string
    rt\_flush\_period searchd_program_configuration_options/rtflush_period
    thread\_stack searchd_program_configuration_options/threadstack
    expansion\_limit searchd_program_configuration_options/expansionlimit
    watchdog searchd_program_configuration_options/watchdog
    sphinxql\_state searchd_program_configuration_options/sphinxqlstate
    ha\_ping\_interval searchd_program_configuration_options/haping_interval
    ha\_period\_karma searchd_program_configuration_options/haperiod_karma
    persistent\_connections\_limit searchd_program_configuration_options/persistentconnections_limit
    rt\_merge\_iops searchd_program_configuration_options/rtmerge_iops
    rt\_merge\_maxiosize searchd_program_configuration_options/rtmerge_maxiosize
    predicted\_time\_costs searchd_program_configuration_options/predictedtime_costs
    shutdown\_timeout searchd_program_configuration_options/shutdowntimeout
    ondisk\_attrs\_default searchd_program_configuration_options/ondiskattrs_default
    query\_log\_min\_msec searchd_program_configuration_options/querylog_min_msec
    agent\_connect\_timeout searchd_program_configuration_options/agentconnect_timeout
    agent\_query\_timeout searchd_program_configuration_options/agentquery_timeout
    agent\_retry\_count searchd_program_configuration_options/agentretry_count
    agent\_retry\_delay searchd_program_configuration_options/agentretry_delay
    hostname\_lookup searchd_program_configuration_options/hostnamelookup
    qcache\_max\_bytes searchd_program_configuration_options/qcachemax_bytes
    qcache\_thresh\_msec searchd_program_configuration_options/qcachethresh_msec
    qcache\_ttl\_sec searchd_program_configuration_options/qcachettl_sec
    grouping\_in\_utc searchd_program_configuration_options/groupingin_utc
    Common section configuration
   options common_section_configuration_options/README
    lemmatizer\_base common_section_configuration_options/lemmatizerbase
    on\_json\_attr\_error common_section_configuration_options/onjson_attr_error
    json\_autoconv\_numbers common_section_configuration_options/jsonautoconv_numbers
    json\_autoconv\_keynames common_section_configuration_options/jsonautoconv_keynames
    rlp\_root common_section_configuration_options/rlproot
    rlp\_environment common_section_configuration_options/rlpenvironment
    rlp\_max\_batch\_size common_section_configuration_options/rlpmax_batch_size
    rlp\_max\_batch\_docs common_section_configuration_options/rlpmax_batch_docs
    plugin\_dir common_section_configuration_options/plugindir
    Version 2.3.2-beta, 09 sep
   2016 version_232-beta,_09_sep_2016
    Version 2.3.1-beta, 03 mar
   2015 version_231-beta,_03_mar_2015
    Version 2.2.11-release, 19 jul
   2016 version_2211-release,_19_jul_2016
    Version 2.2.10-release, 07 sep
   2015 version_2210-release,_07_sep_2015
    Version 2.2.9-release, 16 apr
   2015 version_229-release,_16_apr_2015
    Version 2.2.8-release, 09 mar
   2015 version_228-release,_09_mar_2015
    Version 2.2.7-release, 20 jan
   2015 version_227-release,_20_jan_2015
    Version 2.2.6-release, 13 nov
   2014 version_226-release,_13_nov_2014
    Version 2.2.5-release, 06 oct
   2014 version_225-release,_06_oct_2014
    Version 2.2.4-release, 11 sep
   2014 version_224-release,_11_sep_2014
    Version 2.2.3-beta, 13 may
   2014 version_223-beta,_13_may_2014
    Version 2.2.2-beta, 11 feb
   2014 version_222-beta,_11_feb_2014
    Version 2.2.1-beta, 13 nov
   2013 version_221-beta,_13_nov_2013
    Version 2.1.9-release, 03 jul
   2014 version_219-release,_03_jul_2014
    Version 2.1.8-release, 28 apr
   2014 version_218-release,_28_apr_2014
    Version 2.1.7-release, 30 mar
   2014 version_217-release,_30_mar_2014
    Version 2.1.6-release, 24 feb
   2014 version_216-release,_24_feb_2014
    Version 2.1.5-release, 22 jan
   2014 version_215-release,_22_jan_2014
    Version 2.1.4-release, 18 dec
   2013 version_214-release,_18_dec_2013
    Version 2.1.3-release, 12 nov
   2013 version_213-release,_12_nov_2013
    Version 2.1.2-release, 10 oct
   2013 version_212-release,_10_oct_2013
    Version 2.1.1-beta, 20 feb
   2013 version_211-beta,_20_feb_2013
    Version 2.0.10-release, 22 jan
   2014 version_2010-release,_22_jan_2014
    Version 2.0.9-release, 26 aug
   2013 version_209-release,_26_aug_2013
    Version 2.0.8-release, 26 apr
   2013 version_208-release,_26_apr_2013
    Version 2.0.7-release, 26 mar
   2013 version_207-release,_26_mar_2013
    Version 2.0.6-release, 22 oct
   2012 version_206-release,_22_oct_2012
    Version 2.0.5-release, 28 jul
   2012 version_205-release,_28_jul_2012
    Version 2.0.4-release, 02 mar
   2012 version_204-release,_02_mar_2012
    Version 2.0.3-release, 23 dec
   2011 version_203-release,_23_dec_2011
    Version 2.0.2-beta, 15 nov
   2011 version_202-beta,_15_nov_2011
    Version 2.0.1-beta, 22 apr
   2011 version_201-beta,_22_apr_2011
    Version 1.10-beta, 19 jul 2010 version_110-beta,_19_jul_2010
    Version 0.9.9-release, 02 dec
   2009 version_099-release,_02_dec_2009
    Version 0.9.9-rc2, 08 apr 2009 version_099-rc2,_08_apr_2009
    Version 0.9.9-rc1, 17 nov 2008 version_099-rc1,_17_nov_2008
    Version 0.9.8.1, 30 oct 2008 version_0981,_30_oct_2008
    Version 0.9.8, 14 jul 2008 version_098,_14_jul_2008
    Version 0.9.7, 02 apr 2007 version_097,_02_apr_2007
    Version 0.9.7-rc2, 15 dec 2006 version_097-rc2,_15_dec_2006
    Version 0.9.7-rc1, 26 oct 2006 version_097-rc1,_26_oct_2006
    Version 0.9.6, 24 jul 2006 version_096,_24_jul_2006
    Version 0.9.6-rc1, 26 jun 2006 version_096-rc1,_26_jun_2006
