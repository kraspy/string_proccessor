from enum import Enum, auto

import streamlit as st

st.set_page_config('Replace', '🔁')

st.title('Replace')


class ReplaceType(Enum):
    REPLACE = auto()
    STRIP = auto()
    LSTRIP = auto()
    RSTRIP = auto()
    # TRANSLATE = auto()


replacetype_actions = {
    ReplaceType.REPLACE: ('Replace substring', str.replace),
    ReplaceType.STRIP: ('Remove spaces from both ends', str.strip),
    ReplaceType.LSTRIP: ('Remove spaces from the left side', str.lstrip),
    ReplaceType.RSTRIP: ('Remove spaces from the right side', str.rstrip),
    # ReplaceType.TRANSLATE: ('Replace characters using a table', str.translate),
}


src_text = st.text_area(
    'Your Text',
    key='src_text',
    placeholder='Enter your text here...',
)


replace_type = st.selectbox(
    'Replace Type',
    list(ReplaceType),
    format_func=lambda t: replacetype_actions[t][0],
)

if replace_type is ReplaceType.REPLACE:
    old_col, new_col = st.columns(2)
    with old_col:
        old_substr = st.text_input(
            'Old text',
            key='old_substr',
            placeholder='Substring for replacing',
        )

    with new_col:
        new_substr = st.text_input(
            'New Text',
            key='new_substrsubstr',
            placeholder='New substring',
        )


if st.button('Replace'):
    if replace_type is ReplaceType.REPLACE:
        result = replacetype_actions[replace_type][1](
            src_text,
            old_substr,
            new_substr,
        )
    else:
        result = replacetype_actions[replace_type][1](src_text)

    with st.container(border=True):
        st.html(f'<pre>{result}</pre>')
    st.toast('success', icon='✅')
