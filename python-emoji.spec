Name:		python-emoji
Version:	2.14.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/e/emoji/emoji-%{version}.tar.gz
Summary:	Emoji for Python
URL:		https://pypi.org/project/emoji/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Emoji for Python

%files
%{py_sitedir}/emoji
%{py_sitedir}/emoji-*.*-info
