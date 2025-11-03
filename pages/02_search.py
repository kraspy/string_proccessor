from enum import Enum, auto

import streamlit as st

st.set_page_config('Search', '🔎')

st.title('Search')


class SearchType(Enum):
    FIND = auto()
    STARTSWITH = auto()
    ENDSWITH = auto()
    COUNT = auto()


searchtype_actions = {
    SearchType.FIND: ('Find substring position', str.find),
    SearchType.STARTSWITH: ('Text starts with substring?', str.startswith),
    SearchType.ENDSWITH: ('Text ends with substring?', str.endswith),
    SearchType.COUNT: ('Get count of substring in text', str.count),
}

src_text = st.text_area(
    'Your Text',
    key='src_text',
    placeholder='Enter your text here...',
)

substr = st.text_input(
    'Substring',
    key='substr',
    placeholder='Substring for searching',
)

search_type = st.selectbox(
    'Search Type',
    list(SearchType),
    format_func=lambda t: searchtype_actions[t][0],
)

if st.button('Search'):
    with st.container(border=True):
        st.markdown(searchtype_actions[search_type][1](src_text, substr))
    st.toast('success', icon='✅')
