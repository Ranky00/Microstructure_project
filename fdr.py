##FDR correction for any p-values

import statsmodels.stats.multitest as smt
shin = pd.read_csv('/Users/demoranky/documents/soon.csv')
shin['Bon'] =shin[["P-value"]]*len(shin)
#shin['Bon1'] =smt.multipletests(shin, alpha=0.05, method="bonferroni")
display(shin)

shin.sort_values('Bon')
shin.reset_index(drop=True)
shin['BJ'] = shin[["P-value"]]*len(shin)
shin['BJ1']=shin['BJ'].div(shin.index + 1)
shin['BB'] = shin["Bon"].div(shin.index + 1)
display(shin)

oluwa=shin[shin.BB <0.05]
display(oluwa)
#out_path22 = "/Users/demoranky/documents/fdr_corrected_P-values_ADNI.csv"
#oluwa.to_csv(out_path22, index=True,float_format='%g')