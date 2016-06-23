
# About: Literate Computing for Reproducible Infrastructure README

Literate Computing for Reproducible Infrastructure: インフラ運用をJupyter + Ansibleでおこなう際のお手本Notebookです。

**なお、これらのNotebookはNIIクラウドチーム内で行っている作業の考え方を示すためのもので、環境によってはそのままでは動作しないものもあります。**

[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)


## 関連資料


- [Jupyter notebook を用いた文芸的インフラ運用のススメ - SlideShare](http://www.slideshare.net/nobu758/jupyter-notebook-63167604)
- [Literate Automation（文芸的自動化）についての考察 - めもめも](http://enakai00.hatenablog.com/entry/2016/04/22/204125)



# お手本Notebook

お手本NotebookはこのNotebookと同じディレクトリにあります。Notebookは目的に応じて以下のような命名規則に則って名前がつけられています。

- D(NN)\_(Notebook名) ... インストール関連Notebook
- O(NN)\_(Notebook名) ... 運用関連Notebook
- T(NN)\_(Notebook名) ... テスト関連Notebook

特に、**[Notebook環境Prerequisite](D00_Notebook%E7%92%B0%E5%A2%83Prerequisite.ipynb)は、お手本Notebookが適用可能なNotebook環境、Bind対象であるかどうかを確認するためのNotebook**です。はじめに実施して、これらのお手本Notebookが利用可能な状態かを確認してみてください。

現在、このNotebook環境からアクセス可能なNotebookの一覧を参照するには、以下のセルを実行(`Run cell`)してください。Notebookファイルへのリンクが表示されます。


```python
import re
import os
from IPython.core.display import HTML

ref_notebooks = filter(lambda m: m, map(lambda n: re.match(r'([A-Z][0-9]{2}_.*)\.ipynb', n), os.listdir('.')))
ref_notebooks = sorted(ref_notebooks, key=lambda m: m.group(1))
HTML(''.join(map(lambda m: '<div><a href="{name}" target="_blank">{title}</a></div>'.format(name=m.group(0), title=m.group(1)),
                 ref_notebooks)))
```




<div><a href="D00_Notebook環境Prerequisite.ipynb" target="_blank">D00_Notebook環境Prerequisite</a></div><div><a href="D01_Baremetalマシン確保(OpenStack-AIC).ipynb" target="_blank">D01_Baremetalマシン確保(OpenStack-AIC)</a></div><div><a href="D01_マシン確保(Google Compute Engine).ipynb" target="_blank">D01_マシン確保(Google Compute Engine)</a></div><div><a href="D02_Baremetalマシンセキュリティ設定(@NII).ipynb" target="_blank">D02_Baremetalマシンセキュリティ設定(@NII)</a></div><div><a href="D03_Baremetalマシン削除(OpenStack-AIC).ipynb" target="_blank">D03_Baremetalマシン削除(OpenStack-AIC)</a></div><div><a href="D03_マシン削除(Google Compute Engine).ipynb" target="_blank">D03_マシン削除(Google Compute Engine)</a></div><div><a href="D04_KVMのインストール.ipynb" target="_blank">D04_KVMのインストール</a></div><div><a href="D05_Dockerのインストール.ipynb" target="_blank">D05_Dockerのインストール</a></div><div><a href="O01_CentOS6 VMイメージ作成.ipynb" target="_blank">O01_CentOS6 VMイメージ作成</a></div><div><a href="O01_Ubuntu14.04 VMイメージ作成.ipynb" target="_blank">O01_Ubuntu14.04 VMイメージ作成</a></div><div><a href="O02_VMの作成.ipynb" target="_blank">O02_VMの作成</a></div><div><a href="O03_VMの停止.ipynb" target="_blank">O03_VMの停止</a></div><div><a href="T04_KVMのインストール-Report.ipynb" target="_blank">T04_KVMのインストール-Report</a></div><div><a href="T05_VMの一覧・到達性-Report.ipynb" target="_blank">T05_VMの一覧・到達性-Report</a></div>



## お手本Notebookと証跡Notebook

お手本Notebookを使う場合は、お手本をコピーし、そのコピーを開きます。このように、**お手本と作業証跡は明確に分けながら作業をおこないます。**

また、お手本をコピーする際は、 `YYYYMMDD_NN_` といった実施日を示すプレフィックスを付加することで、後で整理しやすくしています。


## 実際にお手本Notebookを使ってみる

以下のJavaScriptを実行することで、簡単にお手本から作業用Notebookを作成することもできます。

以下のセルを実行すると、Notebook名のドロップダウンリストと[作業開始]ボタンが現れます。
[作業開始]ボタンを押すと、お手本Notebookのコピーを作成した後、自動的にブラウザでコピーが開きます。
Notebookの説明を確認しながら実行、適宜修正しながら実行していってください。


```python
from datetime import datetime
import shutil

def copy_ref_notebook(src):
    prefix = datetime.now().strftime('%Y%m%d') + '_'
    index = len(filter(lambda name: name.startswith(prefix), os.listdir('.'))) + 1
    new_notebook = '{0}{1:0>2}_{2}'.format(prefix, index, src)
    shutil.copyfile(src, new_notebook)
    print(new_notebook)

frags = map(lambda m: '<option value="{name}">{title}</option>'.format(name=m.group(0), title=m.group(1)),
            ref_notebooks)
HTML('''
<script type="text/Javascript">
    function copy_otehon() {
        var sel = document.getElementById('selector');
        IPython.notebook.kernel.execute('copy_ref_notebook("' + sel.options[sel.selectedIndex].value + '")',
                       {'iopub': {'output': function(msg) {
                           window.open(msg.content.text, '_blank')
                       }}});
    }
</script>
<select id="selector">''' + ''.join(frags) + '</select><button onclick="copy_otehon()">作業開始</button>')
```





<script type="text/Javascript">
    function copy_otehon() {
        var sel = document.getElementById('selector');
        IPython.notebook.kernel.execute('copy_ref_notebook("' + sel.options[sel.selectedIndex].value + '")',
                       {'iopub': {'output': function(msg) {
                           window.open(msg.content.text, '_blank')
                       }}});
    }
</script>
<select id="selector"><option value="D00_Notebook環境Prerequisite.ipynb">D00_Notebook環境Prerequisite</option><option value="D01_Baremetalマシン確保(OpenStack-AIC).ipynb">D01_Baremetalマシン確保(OpenStack-AIC)</option><option value="D01_マシン確保(Google Compute Engine).ipynb">D01_マシン確保(Google Compute Engine)</option><option value="D02_Baremetalマシンセキュリティ設定(@NII).ipynb">D02_Baremetalマシンセキュリティ設定(@NII)</option><option value="D03_Baremetalマシン削除(OpenStack-AIC).ipynb">D03_Baremetalマシン削除(OpenStack-AIC)</option><option value="D03_マシン削除(Google Compute Engine).ipynb">D03_マシン削除(Google Compute Engine)</option><option value="D04_KVMのインストール.ipynb">D04_KVMのインストール</option><option value="D05_Dockerのインストール.ipynb">D05_Dockerのインストール</option><option value="O01_CentOS6 VMイメージ作成.ipynb">O01_CentOS6 VMイメージ作成</option><option value="O01_Ubuntu14.04 VMイメージ作成.ipynb">O01_Ubuntu14.04 VMイメージ作成</option><option value="O02_VMの作成.ipynb">O02_VMの作成</option><option value="O03_VMの停止.ipynb">O03_VMの停止</option><option value="T04_KVMのインストール-Report.ipynb">T04_KVMのインストール-Report</option><option value="T05_VMの一覧・到達性-Report.ipynb">T05_VMの一覧・到達性-Report</option></select><button onclick="copy_otehon()">作業開始</button>



## お手本のアーカイブ

以下のセルで、お手本NotebookのZIPアーカイブを作成できます。


```python
ref_notebooks = filter(lambda m: m, map(lambda n: re.match(r'([A-Z][0-9]{2}_.*)\.ipynb', n), os.listdir('.')))
ref_notebooks = sorted(ref_notebooks, key=lambda m: m.group(1))
!zip ref_notebooks-{datetime.now().strftime('%Y%m%d')}.zip README.ipynb {' '.join(map(lambda n: '"' + n.group(0) + '"', ref_notebooks))} scripts/*
```

      adding: README.ipynb (deflated 74%)
      adding: D00_Notebook環境Prerequisite.ipynb (deflated 80%)
      adding: D01_Baremetalマシン確保(OpenStack-AIC).ipynb (deflated 78%)
      adding: D01_マシン確保(Google Compute Engine).ipynb (deflated 79%)
      adding: D02_Baremetalマシンセキュリティ設定(@NII).ipynb (deflated 79%)
      adding: D03_Baremetalマシン削除(OpenStack-AIC).ipynb (deflated 75%)
      adding: D03_マシン削除(Google Compute Engine).ipynb (deflated 74%)
      adding: D04_KVMのインストール.ipynb (deflated 88%)
      adding: D05_Dockerのインストール.ipynb (deflated 87%)
      adding: O01_CentOS6 VMイメージ作成.ipynb (deflated 82%)
      adding: O01_Ubuntu14.04 VMイメージ作成.ipynb (deflated 81%)
      adding: O02_VMの作成.ipynb (deflated 78%)
      adding: O03_VMの停止.ipynb (deflated 80%)
      adding: T04_KVMのインストール-Report.ipynb (deflated 73%)
      adding: T05_VMの一覧・到達性-Report.ipynb (deflated 71%)
      adding: scripts/euca2ools.py (deflated 47%)
      adding: scripts/nova.py (deflated 67%)


こいつを・・・以下のURLからダウンロードできます。


```python
HTML('<a href="../files/{filename}" target="_blank">{filename}</a>' \
     .format(filename='ref_notebooks-' + datetime.now().strftime('%Y%m%d') + '.zip'))
```




<a href="../files/ref_notebooks-20160623.zip" target="_blank">ref_notebooks-20160623.zip</a>




```python

```
