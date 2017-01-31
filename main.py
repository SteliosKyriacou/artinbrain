from inbrain import scholar

options = {'count': 5, 
            'none': 'quantum theory', 
            'no_patents': False, 
            'no_citations': False, 
            'author': 'albert einstein', 
            'cookie_file': None, 
            'citation': None, 
            'some': None, 
            'title_only': True, 
            'pub': None, 
            'allw': None, 
            'version': False, 
            'cluster_id': None, 
            'txt_globals': None, 
            'debug': 0, 
            'phrase': None, 
            'csv_header': None, 
            'txt': None, 
            'csv': None, 
            'after': '1970', 
            'before': None} 

articles = scholar.Search(options)
for article in articles:
    print "title:", article.attrs['title'][0]
    print "url:", article.attrs['url'][0]
    print "year:", article.attrs['year'][0]
    print "num citations:", article.attrs['num_citations'][0]
    print "num versions:",article.attrs['num_versions'][0]
    print "url pdf:",article.attrs['url_pdf'][0]
    print


