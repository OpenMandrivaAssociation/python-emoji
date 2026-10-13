%define module emoji
%bcond tests 1

Name:		python-emoji
Version:	2.16.0
Release:	1
Summary:	Emoji terminal output for Python
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://github.com/carpedm20/emoji
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
Emoji terminal output for Python.

The entire set of Emoji codes as defined by the Unicode consortium is
supported in addition to a bunch of aliases. By default, only the
official list is enabled but doing emoji.emojize(language='alias')
enables both the full list and aliases.

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest
%endif

%files
%doc README.rst
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
