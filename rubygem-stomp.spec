# Generated from stomp-1.1.7.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	stomp

Summary:	Ruby client for the Stomp messaging protocol
Name:		rubygem-%{rbname}

Version:	1.1.7
Release:	1
Group:		Development/Ruby
License:	Apache License
URL:		http://stomp.codehaus.org/
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch
%rename		ruby-stomp

%description
Ruby client for the Stomp messaging protocol

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(examples|spec|test)/'

%install
rm -rf %{buildroot}
%gem_install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/catstomp
%{_bindir}/stompcat
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/catstomp
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/stompcat
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/stomp
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/stomp/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/stomp/ext
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/stomp/ext/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/spec
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/examples
%{ruby_gemdir}/gems/%{rbname}-%{version}/examples/*.rb
