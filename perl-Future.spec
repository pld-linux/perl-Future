#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pnam	Future
Summary:	Future - represent an operation awaiting completion
Name:		perl-Future
Version:	0.41
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{pnam}-%{version}.tar.gz
# Source0-md5:	f83f2ec38a5b3f43fd91bdc886ae151b
URL:		http://search.cpan.org/dist/Future/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Module-Build
%if %{with tests}
BuildRequires:	perl-Test-Identity
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Future object represents an operation that is currently in progress,
or has recently completed. It can be used in a variety of ways to
manage the flow of control, and data, through an asynchronous program.

Some futures represent a single operation and are explicitly marked as
ready by calling the done or fail methods. These are called "leaf"
futures here, and are returned by the new constructor.

Other futures represent a collection of sub-tasks, and are implicitly
marked as ready depending on the readiness of their component futures
as required. These are called "convergent" futures here as they
converge control and data-flow back into one place. These are the ones
returned by the various wait_* and need_* constructors.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Future.pm
%{perl_vendorlib}/Future
%{perl_vendorlib}/Test/Future.pm
%{perl_vendorlib}/Test/Future
%{_mandir}/man3/Future*.3pm*
%{_mandir}/man3/Test::Future*.3pm*
