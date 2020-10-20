# mavonEditor

https://github.com/hinesboy/mavonEditor

https://www.npmjs.com/package/mavon-editor-via

> 安装mavonEditor

```javascript
npm i mavon-editor
```

> vue中使用mavonEditor

```vue
import Vue from 'vue'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
Vue.use(mavonEditor)

<mavon-editor style="height: 100%" ishljg/>
```

# tui-editor

TOASTUI Editor：GFM Markdown WYSIWYG Editor

https://github.com/nhn/tui.editor

https://www.npmjs.com/package/tui-editor

https://nhn.github.io/tui.editor/latest/tutorial-example02-editor-with-horizontal-preview

> 安装tui-editor

```javascript
npm install --save tui-edito
```

> vue中使用Editor

```vue
1.容器
<div id="editorSection"></div>
2.样式
import 'tui-editor/dist/tui-editor.css' // editor's ui
import 'tui-editor/dist/tui-editor-contents.css' // editor's content
import 'codemirror/lib/codemirror.css' // codemirror
import 'highlight.js/styles/github.css' // code block highlight
3.组件
import Editor from 'tui-editor'
4.使用
export default {
    name: 'Editor',
    mounted() {
        const instance = new Editor({
            el: document.querySelector('#editorSection'),
            initialEditType: 'markdown',
            previewStyle: 'vertical',
            initialValue: '# show the content!....'
        })
        instance.getHtml()
    }
}
```

> vue中使用Viewer

```vue
<div id="viewerSection"></div>
import 'tui-editor/dist/tui-editor-contents.css'
import 'highlight.js/styles/github.css'
import Viewer from 'tui-editor/dist/tui-editor-Viewer'
export default {
	name: 'viewer',
    mounted() {
        const instance = new Viewer({
            el: document.querySelector('#viewerSection'),
            initialValue: '# content to be rendered\n> this is paragraph'
        })
        instance.getHtml()
    }
}
```

> 使用注意事项

1. Editor、Viewer不要同时使用，Editor包含Viewer

2. Editor转换为Viewer

```vue
import Editor from 'tui-editor'
const instance = Editor.factory({
    el: document.querySelector('#viewerSection'),
    initialValue: '#content to be rendered',
    viewer: true
})
```

测试发现tui-editor编辑器页面显示不正常























