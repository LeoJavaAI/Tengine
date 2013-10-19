Name: Tengine
Version:  1.5.1      
Release:        1%{?dist}
Summary:       Tengine web server forked out of Nginx 

Group:          Applications/Internet
License:        open BSD license
URL:            http://tengine.taobao.org/download.html
Source0:        tengine-1.5.1.tar.gz

#BuildRequires: 
#Requires:       

%description
Tengine by taboa which enables dso support for nginx


%prep
%setup -n tengine-1.5.1


%build
%_configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE  
%doc README

%config(noreplace) /usr/local/nginx/conf/*
/usr/local/nginx/html/
/usr/local/nginx/sbin/nginx
/usr/local/nginx/sbin/dso_tool

%changelog
