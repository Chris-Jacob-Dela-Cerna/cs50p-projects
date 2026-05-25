

from utils.filter import filter_


def test_filter_extract_html():
    condition = r"^<iframe .*src=\"(https?://(?:www\.)?)youtube.com/embed/(.{11})\" *.*></iframe>$"
    input_ = '<iframe width="560" height="315" src="https://www.youtube.com/embed/FEsL178aHhw?si=d6rVGTIfEucIefRQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    assert filter_(condition, ) == "FEsL178aHhw"