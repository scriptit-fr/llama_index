import pytest
from llama_index.schema import NodeWithScore, TextNode


@pytest.fixture()
def text_node() -> TextNode:
    return TextNode(
        text="hello world",
        metadata={"foo": "bar"},
        embedding=[0.1, 0.2, 0.3],
    )


@pytest.fixture()
def node_with_score(text_node: TextNode) -> NodeWithScore:
    return NodeWithScore(
        node=text_node,
        score=0.5,
    )


def test_node_with_score_passthrough(node_with_score: NodeWithScore) -> None:
    _ = node_with_score.id_
    _ = node_with_score.node_id
    _ = node_with_score.text
    _ = node_with_score.metadata
    _ = node_with_score.embedding
    _ = node_with_score.get_text()
    _ = node_with_score.get_content()
    _ = node_with_score.get_embedding()


def test_text_node_hash() -> None:
    node = TextNode(text="hello", metadata={"foo": "bar"})
    assert (
        node.hash == "aa158bf3388f103cef4bd85b2ca93f343ad8f5e50f58ae4141a35d75a2f21fb0"
    )
    node.set_content("world")
    assert (
        node.hash == "ce6a3cefc3451ecb1ff41ec41a7d7e24354983520d8b2d6f5447be0b6b9b6b99"
    )

    node.text = "new"
    assert (
        node.hash == "bef8ff82498c9aa7d9f9751f441da9a1a1c4e9941bd03c57caa4a602cd5cadd0"
    )
    node2 = TextNode(text="new", metadata={"foo": "bar"})
    assert node2.hash == node.hash
    node3 = TextNode(text="new", metadata={"foo": "baz"})
    assert node3.hash != node.hash
