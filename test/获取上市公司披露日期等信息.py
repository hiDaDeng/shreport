from shreport import SH


cookies = {'Cookie': 'yfx_c_g_u_id_10000042=_ck20040811130118223273975003072; VISITED_MENU=%5B%228312%22%2C%228352%22%5D; VISITED_COMPANY_CODE=%5B%22600277%22%2C%22603383%22%2C%22601857%22%5D; VISITED_STOCK_CODE=%5B%22600277%22%2C%22603383%22%2C%22601857%22%5D; seecookie=%5B600277%5D%3A%u4EBF%u5229%u6D01%u80FD%2C%5B603383%5D%3A%u9876%u70B9%u8F6F%u4EF6%2C%5B601857%5D%3A%u4E2D%u56FD%u77F3%u6CB9; yfx_f_l_v_t_10000042=f_t_1586315581606__r_t_1587454757049__v_t_1587454757049__r_c_1; yfx_mr_10000042=%3A%3Amarket_type_free_search%3A%3A%3A%3Abaidu%3A%3A%3A%3A%3A%3A%3A%3Awww.baidu.com%3A%3A%3A%3Apmf_from_free_search; yfx_mr_f_10000042=%3A%3Amarket_type_free_search%3A%3A%3A%3Abaidu%3A%3A%3A%3A%3A%3A%3A%3Awww.baidu.com%3A%3A%3A%3Apmf_from_free_search; yfx_key_10000042='}

sh = SH(cookies)


#获取浦发银行披露信息
df = sh.disclosure(code='600000')

#只前5条信息
print(df.head())

#存储数据
#df.to_excel('600000.xlsx')