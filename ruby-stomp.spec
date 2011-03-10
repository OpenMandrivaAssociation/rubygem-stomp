%define	oname	stomp

Summary:	Ruby client for the Stomp messaging protocol
Name:		ruby-%{oname}
Version:	1.1
Release:	%mkrel 2
License:	Apache License
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems
Requires:	ruby
BuildArch:	noarch

%description
The Stomp project is the Streaming Text Orientated Messaging Protocol site
(or the Protocol Briefly Known as TTMP and Represented by the symbol :ttmp).
Stomp provides an interoperable wire format so that any of the available
Stomp Clients can communicate with any Stomp Message Broker to provide easy
and widespread messaging interop among languages, platforms and brokers.

%prep

%build

%install
rm -rf %{buildroot}
gem install --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

mv %{buildroot}%{ruby_gemdir}/bin %{buildroot}%{_prefix}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{_bindir}/*
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec

