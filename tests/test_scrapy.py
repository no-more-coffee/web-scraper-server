import json
from importlib import resources

import pytest

from web_scraper_server.spiders import parse_data

FIXTURES_FILES = resources.files("tests.fixtures")

PARSE_FIXTURES = (
    (
        "input.json",
        [
            {
                "image": "https://d18-a.sdn.cz/d_18/c_img_QP_K7/WryKKY.jpeg?fl=res,400,300,3|shr,,20|jpg,90",
                "title": "Praha 10 - Vršovice",
            },
            {
                "image": "https://d18-a.sdn.cz/d_18/c_img_QP_K2/YFwCDJB.jpeg?fl=res,400,300,3|shr,,20|jpg,90",
                "title": "Praha 5 - Hlubočepy",
            },
            {
                "image": "https://d18-a.sdn.cz/d_18/c_img_QQ_Lg/3SZv33.jpeg?fl=res,400,300,3|shr,,20|jpg,90",
                "title": "Praha 10 - Strašnice",
            },
            {
                "image": "https://d18-a.sdn.cz/d_18/c_img_QR_L5/zd8dO0.jpeg?fl=res,400,300,3|shr,,20|jpg,90",
                "title": "Žďár nad Sázavou - Žďár nad Sázavou 3, district Žďár nad Sázavou",
            },
            {
                "image": "https://d18-a.sdn.cz/d_18/c_img_QO_K1/PfUBDuZ.jpeg?fl=res,400,300,3|shr,,20|jpg,90",
                "title": "Benátky nad Jizerou - Benátky nad Jizerou II, district Mladá "
                "Boleslav",
            },
            {
                "image": "https://d18-a.sdn.cz/d_18/c_img_QR_MC/WhzBNL2.jpeg?fl=res,400,300,3|shr,,20|jpg,90",
                "title": "Mladá Boleslav - Mladá Boleslav II, district Mladá Boleslav",
            },
            {
                "image": "https://d18-a.sdn.cz/d_18/c_img_QM_Ka/N49BruQ.jpeg?fl=res,400,300,3|shr,,20|jpg,90",
                "title": "Jablonec nad Nisou - Mšeno nad Nisou, district Jablonec nad Nisou",
            },
            {
                "image": "https://d18-a.sdn.cz/d_18/c_img_QJ_Jg/ZIwCCed.jpeg?fl=res,400,300,3|shr,,20|jpg,90",
                "title": "Pec pod Sněžkou, district Trutnov",
            },
            {
                "image": "https://d18-a.sdn.cz/d_18/c_img_QM_KW/epjPGa.jpeg?fl=res,400,300,3|shr,,20|jpg,90",
                "title": "Pec pod Sněžkou, district Trutnov",
            },
            {
                "image": "https://d18-a.sdn.cz/d_18/c_img_QJ_Jl/fjsB1eB.jpeg?fl=res,400,300,3|shr,,20|jpg,90",
                "title": "Praha 4 - Chodov",
            },
        ],
    ),
)


@pytest.mark.parametrize("input_filename,output", PARSE_FIXTURES)
def test_parse(input_filename, output) -> None:
    input_filepath = FIXTURES_FILES.joinpath(input_filename)
    data = json.loads(input_filepath.read_text())
    result = list(parse_data(data))
    assert result == output
