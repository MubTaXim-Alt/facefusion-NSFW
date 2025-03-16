from typing import Optional

METADATA =\
{
	'name': 'XiMPFusion',
	'description': 'Industry leading face manipulation platform',
	'version': '3.1.1',
	'license': 'MIT',
	'author': 'MubTaXim',
	'url': 'https://github.com/MubTaXim'
}


def get(key : str) -> Optional[str]:
	if key in METADATA:
		return METADATA.get(key)
	return None
