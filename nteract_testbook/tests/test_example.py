import logging

from testbook import testbook

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@testbook("./testbook_example.ipynb", execute=True)
def test_example(tb):
    transform = tb.ref("transform")

    # testing transform
    assert transform(5) == 25

    # testing injected len of df
    tb.inject("assert len(df) == 178")

    # testing output from cell len of df
    assert "178" in tb.cell_output_text(2)