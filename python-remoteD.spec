
%define 	module	remoteD

Summary:	Python module that simplifies multiprocess and IPC programming
Summary(pl.UTF-8):	Moduł Pythona upraszczający programowanie wieloprocesowe i IPC
Name:		python-%{module}
Version:	0.8
Release:	4
License:	BSD-style
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/remoted/%{module}-%{version}.tar.gz
# Source0-md5:	50798875923c85a53872f94ead36c72f
URL:		http://remoted.neurokode.com/
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
Requires:	python >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
remoteD is a Python module that make multiprocess programming and IPC
extremely simple. Each process has access to a shared datastore
maintained by a remoteD server. remoteD servers are auto created for
you when your first process creates a share stub.

%description -l pl.UTF-8
remoteD jest modułem Pythona szalenie ułatwiającym programowanie
wieloprocesowe i IPC. Każdy proces uzyskuje dostęp do dzielonego
zasobu danych utrzymywanego przez serwer remoteD. Serwery remoteD są
tworzone automatycznie, gdy pierwszy z procesów tworzy obszar
dzielony.

%package doc
Summary:	Documentation for remoteD module
Summary(pl.UTF-8):	Dokumentacja do modułu remoteD
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for remoteD Python module.

%description doc -l pl.UTF-8
Pakiet zawierający dokumentację dla modułu Pythona remoteD.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%{py_sitescriptdir}/remoteD.py[oc]

%files doc
%defattr(644,root,root,755)
%doc docs/index.html
