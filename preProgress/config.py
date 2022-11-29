base_url = 'https://m.weibo.cn/detail/'
url = 'https://m.weibo.cn/comments/hotflow?id='

excel_name = r'yyqx_comment.xlsx'



Cookie = {
    'Cookie': 'WEIBOCN_FROM=1110006030; SUB=_2A25OFsbLDeRhGeBM7FYW8ibIwj-IHXVt-OqDrDV6PUJbkdCOLWPdkW1NRNCwEx5ELT8uGVUm0BBD-65kKVXfezHq; MLOGIN=1; _T_WM=30249208298; M_WEIBOCN_PARAMS=oid=4778846533977535&luicode=20000061&lfid=4778846533977535&uicode=20000061&fid=4778846533977535; XSRF-TOKEN=42e0f1'
}

headers = {
    'Sec-Fetch-Mode': 'cors',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',  # 通过ajax请求形式获取数据
    'X-XSRF-TOKEN': 'aa8bed',
    'Accept': 'application/json, text/plain, */*'
}


# 数据id号，要爬取的微博的id号，以及导出到excel对应的sheet名
weiboComment1 = [
    {
    'id':1,
    'weibo_id': 4778846533977535,
    'sheet_name': 'file_tab1',
    },
    {
    'id':2,
    'weibo_id': 4778848081939997,
    'sheet_name': 'file_tab2',
    },{
    'id':3,
    'weibo_id':4778862447697147,
    'sheet_name': 'file_tab3',
    },{
    'id':4,
    'weibo_id':4778863978873965,
    'sheet_name': 'file_tab4',
    },{
    'id':5,
    'weibo_id':4778868978222070,
    'sheet_name': 'file_tab5',
    },{
    'id':6,
    'weibo_id':4778891032139513,
    'sheet_name': 'file_tab6',
    },{
    'id':7,
    'weibo_id':4778927924971858,
    'sheet_name': 'file_tab7',
    },{
    'id':8,
    'weibo_id':4778910031810498,
    'sheet_name': 'file_tab8',
    },{
    'id':9,
    'weibo_id':4778917871751624,
    'sheet_name': 'file_tab9',
    },{
    'id':10,
    'weibo_id':4778942282863557,
    'sheet_name': 'file_tab10',
    },{
    'id':11,
    'weibo_id':4778946375458379,
    'sheet_name': 'file_tab11',
    },{
    'id':12,
    'weibo_id':4778964632994897,
    'sheet_name': 'file_tab12',
    },{
    'id':13,
    'weibo_id':4778964632994897,
    'sheet_name': 'file_tab13',
    },{
    'id':14,
    'weibo_id':4778986204561815,
    'sheet_name': 'file_tab14',
    },{
    'id':15,
    'weibo_id':4779041514586791,
    'sheet_name': 'file_tab15',
    },{
    'id':16,
    'weibo_id':4779097135779543,
    'sheet_name': 'file_tab16',
    },{
    'id':17,
    'weibo_id':4779123396318627,
    'sheet_name': 'file_tab17',
    },{
    'id':18,
    'weibo_id':4779133920349282,
    'sheet_name': 'file_tab18',
    },{
    'id':19,
    'weibo_id':4779180141053010,
    'sheet_name': 'file_tab19',
    },{
    'id':20,
    'weibo_id':4779307454694252,
    'sheet_name': 'file_tab20',
    },{
    'id':21,
    'weibo_id':4779309947158565,
    'sheet_name': 'file_tab21',
    },{
    'id':22,
    'weibo_id':4779479266236489,
    'sheet_name': 'file_tab22',
    },{
    'id':23,
    'weibo_id':4779635269697984,
    'sheet_name': 'file_tab23',
    },{
    'id':24,
    'weibo_id':4779675349683648,
    'sheet_name': 'file_tab24',
    },{
    'id':25,
    'weibo_id':4780542707371104,
    'sheet_name': 'file_tab25',
    },{
    'id':26,
    'weibo_id':4782736927885093,
    'sheet_name': 'file_tab26',
    },{
    'id':27,
    'weibo_id':4782738895275023,
    'sheet_name': 'file_tab27',
    },{
    'id':28,
    'weibo_id':4782754682899606,
    'sheet_name': 'file_tab28',
    },{
    'id':29,
    'weibo_id':4807719029312456,
    'sheet_name': 'file_tab29',
    },{
    'id':30,
    'weibo_id':4807720760510200,
    'sheet_name': 'file_tab30',
    },{
    'id':31,
    'weibo_id':4807780567351794,
    'sheet_name': 'file_tab31',
    },{
    'id':32,
    'weibo_id':4807782169842058,
    'sheet_name': 'file_tab32',
    },{
    'id':33,
    'weibo_id':4778925606311712,
    'sheet_name': 'file_tab33',
    },{
    'id':34,
    'weibo_id':4778951220139013,
    'sheet_name': 'file_tab34',
    },{
    'id':35,
    'weibo_id':4778937471999284,
    'sheet_name': 'file_tab35',
    },
    {
    'id':36,
    'weibo_id':4778958292262935,
    'sheet_name': 'file_tab36',
    },{
    'id':37,
    'weibo_id':4779628642701088,
    'sheet_name': 'file_tab37',
    },{
    'id':38,
    'weibo_id':4779916215977663,
    'sheet_name': 'file_tab38',
    },{
    'id':39,
    'weibo_id':4779254946204463,
    'sheet_name': 'file_tab39',
    },
]


weiboComment =[
    {
    'id':1,
    'weibo_id':4788267607654711,
    'sheet_name': 'file_tab1',
    },{
    'id':2,
    'weibo_id':4788963917959558,
    'sheet_name': 'file_tab2',
    },{
    'id':3,
    'weibo_id':4789243744357044,
    'sheet_name': 'file_tab3',
    },{
    'id':4,
    'weibo_id':4789340925854721,
    'sheet_name': 'file_tab4',
    },{
    'id':5,
    'weibo_id':4789340717189650,
    'sheet_name': 'file_tab5',
    },{
    'id':6,
    'weibo_id':4788907189207606,
    'sheet_name': 'file_tab6',
    },{
    'id':7,
    'weibo_id':4801732532772138,
    'sheet_name': 'file_tab7',
    },{
    'id':8,
    'weibo_id':4789005343785577,
    'sheet_name': 'file_tab8',
    },{
    'id':9,
    'weibo_id':4788659847693859,
    'sheet_name': 'file_tab9',
    },{
    'id':10,
    'weibo_id':4788723629425246,
    'sheet_name': 'file_tab10',
    },{
    'id':11,
    'weibo_id':4788734866492774,
    'sheet_name': 'file_tab11',
    },{
    'id':12,
    'weibo_id':4788685431643280,
    'sheet_name': 'file_tab12',
    },{
    'id':13,
    'weibo_id':4791780220864226,
    'sheet_name': 'file_tab13',
    },{
    'id':14,
    'weibo_id':4788659829868344,
    'sheet_name': 'file_tab14',
    },{
    'id':15,
    'weibo_id':4788680419705972,
    'sheet_name': 'file_tab15',
    },{
    'id':16,
    'weibo_id':4790392963469793,
    'sheet_name': 'file_tab15',
    },{
    'id':17,
    'weibo_id':4792513497923632,
    'sheet_name': 'file_tab15',
    },{
    'id':18,
    'weibo_id':4792516546920762,
    'sheet_name': 'file_tab15',
    },{
    'id':19,
    'weibo_id':4753846863136900,
    'sheet_name': 'file_tab19',
    },{
    'id':20,
    'weibo_id':4753847446933336,
    'sheet_name': 'file_tab20',
    },{
    'id':21,
    'weibo_id':4790904625828722,
    'sheet_name': 'file_tab21',
    },{
    'id':22,
    'weibo_id':4791046334843611,
    'sheet_name': 'file_tab22',
    },{
    'id':23,
    'weibo_id':4792167307940858,
    'sheet_name': 'file_tab23',
    },{
    'id':24,
    'weibo_id':4792208358639704,
    'sheet_name': 'file_tab24',
    },{
    'id':25,
    'weibo_id':4792286258663021,
    'sheet_name': 'file_tab25',
    },{
    'id':26,
    'weibo_id':4792313526617456,
    'sheet_name': 'file_tab26',
    },
    {
    'id':27,
    'weibo_id':4792166097096061,
    'sheet_name': 'file_tab27',
    },{
    'id':28,
    'weibo_id':4792173398068014,
    'sheet_name': 'file_tab28',
    },
    {
    'id':29,
    'weibo_id':4791791067074803,
    'sheet_name': 'file_tab29',
    },{
    'id':30,
    'weibo_id':4793002122544963,
    'sheet_name': 'file_tab30',
    },{
    'id':31,
    'weibo_id':4791227734038316,
    'sheet_name': 'file_tab31',
    },{
    'id':32,
    'weibo_id':4788710531666794,
    'sheet_name': 'file_tab32',
    },{
    'id':33,
    'weibo_id':4805056652121088,
    'sheet_name': 'file_tab33',
    },{
    'id':34,
    'weibo_id':4791798289142666,
    'sheet_name': 'file_tab34',
    },






]