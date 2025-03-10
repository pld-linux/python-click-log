%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		click_log
%define		pypi_name	click-log
Summary:	Integrates logging with click
Name:		python-click-log
Version:	0.3.2
Release:	6
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/click-log/
Source0:	https://files.pythonhosted.org/packages/source/c/click-log/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	5c9244f0fa5b3557220396e32d32daf2
URL:		https://pypi.org/project/click-log/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Integrates logging with click.

%package -n python3-click-log
Summary:	Integrates logging with click
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-click-log
Integrates logging with click.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-click-log
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
