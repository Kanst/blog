mySettings = {
    previewParserPath:  '/markitup/preview/',
    onShiftEnter:       {keepDefault:false, openWith:'\n\n'},
    markupSet: [
        {name:'Example block', key:'Q', openWith:'> '},
        {name:'Inline example', key:'E', openWith:'<example>', closeWith:'</example>'},
        {name:'First Level Heading', key:"3", placeHolder:'Your title here...', closeWith:function(markItUp) { return miu.markdownTitle(markItUp, '=') } },
        {name:'Second Level Heading', key:"4", placeHolder:'Your title here...', closeWith:function(markItUp) { return miu.markdownTitle(markItUp, '-') } },
        {name:'Heading 3', key:"5", openWith:'### ', placeHolder:'Your title here...' },
        {name:'Bold', key:'B', openWith:'**', closeWith:'**'},
        {name:'Italic', key:'I', openWith:'*', closeWith:'*'},
        {separator:'---------------' },
        {name:'Bulleted List', openWith:'- ' },
        {name:'Numeric List', openWith:function(markItUp) {
            return markItUp.line+'. ';
        }},
        {separator:'---------------'},    
        {name:'Quotes', openWith:'> '},
        {name:'Code Block / Code', openWith:'(!(\t|!|`)!)', closeWith:'(!(`)!)'},
        {separator:'---------------'},
        {name:'Preview', call:'preview', className:"preview"}
    ]
}

// mIu nameSpace to avoid conflict.
miu = {
    markdownTitle: function(markItUp, char) {
        heading = '';
        n = $.trim(markItUp.selection||markItUp.placeHolder).length;
        for(i = 0; i < n; i++) {
            heading += char;
        }
        return '\n'+heading+'\n';
    }
}