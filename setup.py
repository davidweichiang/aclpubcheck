from setuptools import setup


install_requires = [
	"tqdm",
	"termcolor",
	"pandas",
	"pdfplumber"
]


setup(
	name="aclpubcheck",
	install_requires=install_requires,
	version="0.1",
	scripts=[]
)
