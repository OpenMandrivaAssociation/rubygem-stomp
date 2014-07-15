%define	oname	stomp

Summary:	Ruby client for the Stomp messaging protocol
Name:		rubygem-%{oname}
Version:	1.1.7
Release:	3
License:	Apache License
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRequires:	ruby-RubyGems
Requires:	ruby
BuildArch:	noarch
%rename ruby-%{oname}

%description
The Stomp project is the Streaming Text Orientated Messaging Protocol site
(or the Protocol Briefly Known as TTMP and Represented by the symbol :ttmp).
Stomp provides an interoperable wire format so that any of the available
Stomp Clients can communicate with any Stomp Message Broker to provide easy
and widespread messaging interop among languages, platforms and brokers.

%prep

%build

%install
gem install --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

mv %{buildroot}%{ruby_gemdir}/bin %{buildroot}%{_prefix}

%clean

%files
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{_bindir}/*
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec



