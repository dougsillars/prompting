import pytest

from prompting.tools import MockDataset, CodingDataset, WikiDataset, StackOverflowDataset, DateQADataset, MathDataset




DATASETS = [
    MockDataset,
    CodingDataset,
    WikiDataset,
    # StackOverflowDataset,
    DateQADataset,
    MathDataset,
]

CONTEXTS = {
    WikiDataset: {"text": "This is a context.", "title": "this is a title", "categories": ['some','categories']},
    CodingDataset: {"code": "This is code","repo_name":'prompting',"path":'this/is/a/path', "language":'python'},
    MathDataset: {"problem": "This is a problem","solution":'3.1415','topic':'math','subtopic':'calculus'},
    DateQADataset: {"section": "Events", "event":"1953 - Battle of Hastings in UK", 'date':"1 January"},
}


@pytest.mark.parametrize('dataset', DATASETS)
def test_create_dataset(dataset):
    data = dataset()
    assert data is not None


@pytest.mark.parametrize('dataset', DATASETS)
def test_next_returns_dict(dataset):
    data = dataset()
    assert type(data.next()) == dict

@pytest.mark.parametrize('dataset', DATASETS)
def test_next_returns_fields(dataset):
    data = dataset()
    context = data.next()
    for field in CONTEXTS[dataset].keys():
        assert field in context