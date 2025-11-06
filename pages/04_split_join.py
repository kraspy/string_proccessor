from enum import Enum, auto

import streamlit as st

st.set_page_config('Splitting/Joining', '🪓')


class OperationType(Enum):
    SPLIT = auto()
    SPLITLINES = auto()
    JOIN = auto()


operation_actions = {
    OperationType.SPLIT: (
        'Split text by a symbol',
        str.split,
    ),
    OperationType.SPLITLINES: (
        'Split text into lines',
        str.splitlines,
    ),
    OperationType.JOIN: (
        'Join text using a new symbol after splitting',
        str.join,
    ),
}


st.title('Split/Join')

src_text = st.text_area('Your text')

selected_operation = st.selectbox(
    'Operation type',
    OperationType,
    format_func=lambda op: operation_actions[op][0],
)


if not selected_operation == OperationType.SPLITLINES:
    splitter = st.text_input('Splitter', ',')


if selected_operation == OperationType.JOIN:
    connector = st.text_input('Connector', '-')

st.checkbox('Strip elements', key='strip_elements')


if st.button('Transform'):
    if selected_operation == OperationType.SPLIT:
        result = operation_actions[selected_operation][1](src_text, splitter)
    elif selected_operation == OperationType.SPLITLINES:
        result = operation_actions[selected_operation][1](src_text)
    elif selected_operation == OperationType.JOIN:
        splited_elements = src_text.split(splitter)
        result = connector.join(
            [el.strip() for el in splited_elements]
            if st.session_state['strip_elements']
            else splited_elements
        )

    st.markdown('**Elements**:')
    with st.container(
        border=True, horizontal=True, horizontal_alignment='left'
    ):
        if isinstance(result, list):
            if st.session_state['strip_elements']:
                result = list(map(str.strip, result))
            for el in result:
                st.badge(el, width='content')
        else:
            st.text(result)
    st.toast('success', icon='✅')
