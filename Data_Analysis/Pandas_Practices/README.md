# Pandas Tricks

@name=SharkChilli_zx

查看pandas版本: `pd.show_versions()` <br>
更新pandas版本: `!pip install --upgrade pandas`

---

## [pandas exercises](https://github.com/guipsamora/pandas_exercises)

### 01 - Getting & Knowing the Data
* [**Tutorial 1.1**](https://nbviewer.jupyter.org/github/SharkChilli-Cyrus/Data-Science/blob/master/Data-Analysis/Pandas/01_Getting_%26_Knowing_The_Data/Tut_1_1.ipynb)
    * 读取 URL 地址的 dataset
        * Note: sep
    * .info()
    * 显示 DataFrame 的 columns & index 
    * [**groupby**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)
        * > c = chipo.groupby('item_name')<br>
          > c = c.sum()<br>
          > c = c.sort_values(['quantity'], ascending=False)
    * 列排序 sort_values
    * [**lambda**](https://www.zhihu.com/question/20125256) & [**apply**](https://www.jianshu.com/p/c41627028f58)
    * 列运算 np.muptiply
    * 计数 [**value_counts**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html) & [**count()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.count.html)
        * > dollarizer = lambda x: float(x[1:-1])<br>
          > chipo['item_price'] = chipo['item_price'].apply(dollarizer)
* [**Tutorial 1.2**](https://nbviewer.jupyter.org/github/SharkChilli-Cyrus/Data-Science/blob/master/Data-Analysis/Pandas/01_Getting_%26_Knowing_The_Data/Tut_1_2.ipynb)
    * pd.read_table(url, sep= , index_col= )
    * df.descripbe()
    * df['colname'].[nunique()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.nunique.html)
    * df['colname'].**value_counts()**
* [**Tutorial 1.3**](https://nbviewer.jupyter.org/github/SharkChilli-Cyrus/Data-Science/blob/master/Data-Analysis/Pandas/01_Getting_%26_Knowing_The_Data/Tut_1_3.ipynb)
    * [**loc**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html)
    * values

### 02 - Filtering & Sorting
* [**Tutorial 2.1**](https://nbviewer.jupyter.org/github/SharkChilli-Cyrus/Data-Science/blob/master/Data-Analysis/Pandas/02_Filtering_%26_Sorting/Tut_2_1.ipynb)
    * import warnings
    * import IPython.core.interactiveshell
    * [**列表生成式**](https://www.liaoxuefeng.com/wiki/1016959663602400/1017317609699776)
    * 去重
        * [dulicated](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html)
        * [drop_duplicates](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html)
    * **Select Data**
    * sort_values
* [**Tutorial 2.2**](https://nbviewer.jupyter.org/github/SharkChilli-Cyrus/Data-Science/blob/master/Data-Analysis/Pandas/02_Filtering_%26_Sorting/Tut_2_2.ipynb)
    * [**iloc**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html)
    * round()
    * [**选取以G开头的Team - str.startswith()**](https://www.tutorialspoint.com/python/string_startswith.htm)
    * **`loc[condition, col_list]`**
        * > euro12.loc[euro12['Team'].isin(['England', 'Italy', 'Russia']), ['Team', 'Shooting Accuracy']]
* [**Tutorial 2.3**](https://nbviewer.jupyter.org/github/SharkChilli-Cyrus/Data-Science/blob/master/Data-Analysis/Pandas/02_Filtering_%26_Sorting/Tut_2_3.ipynb)
    * [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
    * [set_index](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html)
    * [**loc & iloc**](https://www.okcode.net/article/68173)

### 03 - Grouping
* [**Tutorial 3.1**](https://nbviewer.jupyter.org/github/SharkChilli-Cyrus/Data-Science/blob/master/Data-Analysis/Pandas/03_Grouping/Tut_3_1.ipynb)
    * [**groupby**](https://www.yiibai.com/pandas/python_pandas_groupby.html)
    * grouped.describe
    * grouped.agg
    * grouped.transform
    * grouped.filter
* [**Tutorial 3.2**](https://nbviewer.jupyter.org/github/SharkChilli-Cyrus/Data-Science/blob/master/Data-Analysis/Pandas/03_Grouping/Tut_3_2.ipynb)
    * apply
    * agg
    * div
* [**Tutorial 3.3**](https://nbviewer.jupyter.org/github/SharkChilli-Cyrus/Data-Science/blob/master/Data-Analysis/Pandas/03_Grouping/Tut_3_3.ipynb)
    * DataFrame
    * unstack
    * size
    * for key, value in df.groupby()

### 04 - Apply
* [**Tutorial 4.1**](https://nbviewer.jupyter.org/github/SharkChilli-Cyrus/Data-Science/blob/master/Data-Analysis/Pandas/04_Apply/Tut_4_1.ipynb)
    * loc[:, colname1:colname2]
    * lambda
    * str.capitalize
    * apply
    * [applymap](https://www.jianshu.com/p/f35b4ba2c64a)
* [**Tutorial 4.2**](https://nbviewer.jupyter.org/github/SharkChilli-Cyrus/Data-Science/blob/master/Data-Analysis/Pandas/04_Apply/Tut_4_2.ipynb)
    * [del & df.drop](https://stackoverflow.com/questions/47426089/python-del-vs-pandas-drop)
    * [resample](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html)
    * [<u>To learn more about Offset Aliases</u>](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)
    * [set_index](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html)
    * index.name
    * drop index name
    * [idxmax](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.idxmax.html)

### 05 - Merge
* [**Tutorial 5.1**](https://nbviewer.jupyter.org/github/SharkChilli-Cyrus/Data-Science/blob/master/Data-Analysis/Pandas/05_Merge/Tut_5_1.ipynb)
    * append
    * np.random.randint
    * [**reset_index**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html)
* [**Tutorial 5.2**](https://nbviewer.jupyter.org/github/SharkChilli-Cyrus/Data-Science/blob/master/Data-Analysis/Pandas/05_Merge/Tut_5_2.ipynb)
    * [concat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)
    * [merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html)


### Other
- [ ] [Pandas Docs](https://pandas.pydata.org/pandas-docs/version/0.25/)
- [ ] [pandas_profiling Docs](https://pandas-profiling.github.io/pandas-profiling/docs/)

---
## How to read a jupyter file (xxx.ipynb)

**Example 1**: --> Use *nbviewer* for Notebook

**https://nbviewer.jupyter.org/github**

1. Choose a .ipynb file and copy the github path:<br>
`https://github.com/`SharkChilli-Cyrus/Machine_Learning/blob/master/ML_Course_Notebook/Machine_Learning_Notebook.ipynb

2. Change it into:<br>
`https://nbviewer.jupyter.org/github/`SharkChilli-Cyrus/Machine_Learning/blob/master/ML_Course_Notebook/Machine_Learning_Notebook.ipynb


**Example 2**: --> Use *Colaboratory* for Code

[Colaboratory](https://colab.research.google.com/notebooks/welcome.ipynb)

For more information: [Using Google Colab with GitHub](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)


---
## Links:
1. [ ] [pandas cheat sheet](https://www.datacamp.com/community/blog/python-pandas-cheat-sheet?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=1t1&utm_creative=229765585183&utm_targetid=dsa-473406587915&utm_loc_interest_ms=&utm_loc_physical_ms=9062542&gclid=EAIaIQobChMIw8mCg_vr5QIVQQwrCh32AgxdEAAYASAAEgL6KPD_BwE)


![](https://i.imgur.com/w5lY0yS.png)