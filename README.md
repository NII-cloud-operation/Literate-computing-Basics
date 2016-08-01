
# About: Literate Computing for Reproducible Infrastructure README

---

**Literate Computing for Reproducible Infrastructure:** Notebooks for operations of infrastructure.  Operational procedures and considerations are described literatelly and reproducibly using Jupyter and Ansible. 
These are a kind of exemplary copybooks which present how NII cloud operation does, thus you may need appropriate modification on your practice.

インフラ運用をJupyter + Ansibleでおこなう際のお手本Notebookです。<br>
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

ref_notebooks = filter(lambda m: m, map(lambda n: re.match(r'([A-Z][0-9][0-9a-z]+_.*)\.ipynb', n), os.listdir('.')))
ref_notebooks = sorted(ref_notebooks, key=lambda m: m.group(1))
HTML(''.join(map(lambda m: '<div><a href="{name}" target="_blank">{title}</a></div>'.format(name=m.group(0), title=m.group(1)),
                 ref_notebooks)))
```




<div><a href="D00_Prerequisits for Literate Computing via Notebooks.ipynb" target="_blank">D00_Prerequisits for Literate Computing via Notebooks</a></div><div><a href="D01_GCE - Set! Go! (Google Compute Engine).ipynb" target="_blank">D01_GCE - Set! Go! (Google Compute Engine)</a></div><div><a href="D02_Docker - Ready! on Ubuntu and Set! Go!.ipynb" target="_blank">D02_Docker - Ready! on Ubuntu and Set! Go!</a></div><div><a href="D03_KVM - Ready! on CentOS.ipynb" target="_blank">D03_KVM - Ready! on CentOS</a></div><div><a href="D03b_KVM - Set! CentOS6.ipynb" target="_blank">D03b_KVM - Set! CentOS6</a></div><div><a href="D03b_KVM - Set! Ubuntu 14.04.ipynb" target="_blank">D03b_KVM - Set! Ubuntu 14.04</a></div><div><a href="D03c_KVM - Go! VM.ipynb" target="_blank">D03c_KVM - Go! VM</a></div><div><a href="D90_Postscript - Operational Policy Settings; Security etc. (to be elaborated).ipynb" target="_blank">D90_Postscript - Operational Policy Settings; Security etc. (to be elaborated)</a></div><div><a href="O03_GCE - Destroy VM (Google Compute Engine).ipynb" target="_blank">O03_GCE - Destroy VM (Google Compute Engine)</a></div><div><a href="O03_KVM - Destroy VM on KVM.ipynb" target="_blank">O03_KVM - Destroy VM on KVM</a></div><div><a href="T03_KVM - Confirm KVM is healthy .ipynb" target="_blank">T03_KVM - Confirm KVM is healthy </a></div><div><a href="T03_KVM - Status Report of running VMs.ipynb" target="_blank">T03_KVM - Status Report of running VMs</a></div>



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
<select id="selector"><option value="D00_Prerequisits for Literate Computing via Notebooks.ipynb">D00_Prerequisits for Literate Computing via Notebooks</option><option value="D01_GCE - Set! Go! (Google Compute Engine).ipynb">D01_GCE - Set! Go! (Google Compute Engine)</option><option value="D02_Docker - Ready! on Ubuntu and Set! Go!.ipynb">D02_Docker - Ready! on Ubuntu and Set! Go!</option><option value="D03_KVM - Ready! on CentOS.ipynb">D03_KVM - Ready! on CentOS</option><option value="D03b_KVM - Set! CentOS6.ipynb">D03b_KVM - Set! CentOS6</option><option value="D03b_KVM - Set! Ubuntu 14.04.ipynb">D03b_KVM - Set! Ubuntu 14.04</option><option value="D03c_KVM - Go! VM.ipynb">D03c_KVM - Go! VM</option><option value="D90_Postscript - Operational Policy Settings; Security etc. (to be elaborated).ipynb">D90_Postscript - Operational Policy Settings; Security etc. (to be elaborated)</option><option value="O03_GCE - Destroy VM (Google Compute Engine).ipynb">O03_GCE - Destroy VM (Google Compute Engine)</option><option value="O03_KVM - Destroy VM on KVM.ipynb">O03_KVM - Destroy VM on KVM</option><option value="T03_KVM - Confirm KVM is healthy .ipynb">T03_KVM - Confirm KVM is healthy </option><option value="T03_KVM - Status Report of running VMs.ipynb">T03_KVM - Status Report of running VMs</option></select><button onclick="copy_otehon()">作業開始</button>



## お手本のアーカイブ

以下のセルで、お手本NotebookのZIPアーカイブを作成できます。


```python
ref_notebooks = filter(lambda m: m, map(lambda n: re.match(r'([A-Z][0-9][0-9a-z]+_.*)\.ipynb', n), os.listdir('.')))
ref_notebooks = sorted(ref_notebooks, key=lambda m: m.group(1))
!zip ref_notebooks-{datetime.now().strftime('%Y%m%d')}.zip README.ipynb {' '.join(map(lambda n: '"' + n.group(0) + '"', ref_notebooks))} scripts/*
```

      adding: README.ipynb (deflated 73%)
      adding: D00_Prerequisits for Literate Computing via Notebooks.ipynb (deflated 79%)
      adding: D01_GCE - Set! Go! (Google Compute Engine).ipynb (deflated 78%)
      adding: D02_Docker - Ready! on Ubuntu and Set! Go!.ipynb (deflated 87%)
      adding: D03_KVM - Ready! on CentOS.ipynb (deflated 88%)
      adding: D03b_KVM - Set! CentOS6.ipynb (deflated 82%)
      adding: D03b_KVM - Set! Ubuntu 14.04.ipynb (deflated 81%)
      adding: D03c_KVM - Go! VM.ipynb (deflated 77%)
      adding: D90_Postscript - Operational Policy Settings; Security etc. (to be elaborated).ipynb (deflated 78%)
      adding: O03_GCE - Destroy VM (Google Compute Engine).ipynb (deflated 74%)
      adding: O03_KVM - Destroy VM on KVM.ipynb (deflated 79%)
      adding: T03_KVM - Confirm KVM is healthy .ipynb (deflated 73%)
      adding: T03_KVM - Status Report of running VMs.ipynb (deflated 71%)
      adding: scripts/euca2ools.py (deflated 47%)
      adding: scripts/nova.py (deflated 67%)


こいつを・・・以下のURLからダウンロードできます。


```python
HTML('<a href="../files/{filename}" target="_blank">{filename}</a>' \
     .format(filename='ref_notebooks-' + datetime.now().strftime('%Y%m%d') + '.zip'))
```




<a href="../files/ref_notebooks-20160801.zip" target="_blank">ref_notebooks-20160801.zip</a>




```python

```
