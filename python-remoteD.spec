# $Revision: 1.2 $ $Date: 2004-06-04 22:04:08 $

%include	/usr/lib/rpm/macros.python
%define 	module	remoteD

Summary:	Python module that simplifies multiprocess and IPC programming
Summary(pl):	Modu³ Pythona upraszczaj±cy programowanie wieloprocesowe i IPC
Name:		python-%{module}
Version:	0.8
Release:	1
License:	BSD-style
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/remoted/%{module}-%{version}.tar.gz
# Source0-md5:	50798875923c85a53872f94ead36c72f
URL:		http://remoted.neurokode.com/
BuildRequires:	python-devel >= 2.3
Requires:	python >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
remoteD is a Python module that make multiprocess programming and IPC
extremely simple. Each process has access to a shared datastore
maintained by a remoteD server. remoteD servers are auto created for
you when your first process creates a share stub.

%description -l pl
remoteD jest modu³em Pythona szalenie u³atwiaj±cym programowanie
wieloprocesowe i IPC. Ka¿dy proces uzyskuje dostêp do dzielonego
zasobu danych utrzymywanego przez serwer remoteD. Serwery remoteD s±
tworzone automatycznie, gdy pierwszy z procesów tworzy obszar
dzielony.

%package doc
Summary:	Documentation for remoteD module
Summary(pl):	Dokumentacja do modu³u remoteD
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for remoteD Python module.

%description doc -l pl
Pakiet zawieraj±cy dokumentacjê dla modu³u Pythona remoteD.

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
