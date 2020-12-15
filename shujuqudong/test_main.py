import pytest
import yaml

class TestMain:
    @pytest.mark.parametrize("value1,value2", yaml.safe_load(open("./test_main.yaml")))
    def test_main(self, value1, value2):
        print(value1)
        print(value2)