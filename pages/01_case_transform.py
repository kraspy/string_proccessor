from enum import Enum, auto

import streamlit as st

st.set_page_config('Case Transform', '🔠')

st.title('Case Transform')


src_text = st.text_area(
    'Your Text',
    key='src_text',
    placeholder='Enter your text here...',
)


class TrasnformTypes(Enum):
    UPPER = auto()
    LOWER = auto()
    CAPITALIZE = auto()
    TITLE = auto()
    SWAPCASE = auto()


transform_actions = {
    TrasnformTypes.UPPER: (
        'Convert all letters to uppercase',
        str.upper,
    ),
    TrasnformTypes.LOWER: (
        'Convert all letters to lowercase',
        str.lower,
    ),
    TrasnformTypes.CAPITALIZE: (
        'Capitalize the first character of the text',
        str.capitalize,
    ),
    TrasnformTypes.TITLE: (
        'Capitalize the first letter of each word',
        str.title,
    ),
    TrasnformTypes.SWAPCASE: (
        'Swap the case of all letters',
        str.swapcase,
    ),
}

transform_type = st.selectbox(
    'Transform Type',
    list(TrasnformTypes),
    format_func=lambda t: transform_actions[t][0],
)

if st.button('Transform', 'btn_transform', type='secondary'):
    with st.container(border=True):
        st.markdown(
            transform_actions[transform_type][1](src_text),
        )
    st.toast('Success', icon='✅')
