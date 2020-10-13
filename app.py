import streamlit as st
from transformers import pipeline, set_seed
from transformers.pipelines import TextGenerationPipeline


class TextGenerator:
    def __init__(self):
        self.generator: TextGenerationPipeline
        self.max_length = 300
        set_seed(1)

    def load_generator(self) -> None:
        self.generator = pipeline('text-generation', model='gpt2')

    def generate_text(self, starting_text: str) -> str:
        return self.generator(starting_text,
                              max_length=self.max_length,
                              num_return_sequences=1)[0]['generated_text']


@st.cache(allow_output_mutation=True)
def instantiate_generator():
    generator = TextGenerator()
    generator.load_generator()
    return generator


if __name__ == '__main__':
    st.title('Text Completion using GPT-2')
    starting_text = st.text_area('Type any phrase/keyword...')
    generator = instantiate_generator()

    if starting_text:
        response = generator.generate_text(starting_text)
        st.markdown(f'Result: {response}')