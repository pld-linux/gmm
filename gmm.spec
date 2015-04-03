Summary:	A generic C++ template library for sparse, dense and skyline matrices
Name:		gmm
Version:	4.3
Release:	1
License:	LGPL v2+
Group:		Development/Libraries
URL:		http://home.gna.org/getfem/gmm_intro
Source0:	http://download.gna.org/getfem/stable/%{name}-%{version}.tar.gz
# Source0-md5:	f64441d4f85c6a37b8ae1cc70649b795
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# to fool configure script
%define		_target_platform	%{_host_cpu}-%{_target_vendor}-%{_target_os}%{?_gnu}

# nothing to put there
%define		_enable_debug_packages	0

%description
A generic C++ template library for sparse, dense and skyline matrices.

%package devel
Summary:	A generic C++ template library for sparse, dense and skyline matrices
Group:		Development/Libraries

%description devel
A generic C++ template library for sparse, dense and skyline matrices.

%prep
%setup -q

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%{_includedir}/gmm
