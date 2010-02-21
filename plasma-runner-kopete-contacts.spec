
Summary:        Kopete contacts KDE runner
Name:           plasma-runner-kopete-contacts
Version:        0.4
Release:        %mkrel 1
Source:         http://kde-apps.org/CONTENT/content-files/105263-krunner-kopete-contacts-%{version}.tar.gz
License:        GPLv2+                                         
Group:          Graphical desktop/KDE                          
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:            http://kde-apps.org/content/show.php/KRunner+Kopete+Contacts?content=105263
#BuildRequires:  kdelibs4-devel                       
BuildRequires:  kdenetwork4-devel
Requires:	kopete
Obsoletes:	kopete-kde-runner

%description
Kopete Contacts is a KRunner plugins that allows you to open chat with your Kopete contact just by typing it's 
name!
 
 Cool improvement for people like me who are lazy to open the Kopete window :-)
 
 In future I'd like to add configuration dialog to enable filtering offline contacts etc...for now this is just 
first release, so no big expectations (but it works :D ) 
 
 For those of you who are extremely lazy I've implemented new function. You can now change your Kopete status 
(all accounts) by typing "status status_name". Supported are only default statuses (online,offline,away,busy and 
invisible).
 

%files
%defattr(-,root,root)
%doc COPYING
%{_kde_libdir}/kde4/*.so
%{_kde_services}/*
#%{_datadir}/pixmaps/vbox-runner/*
#--------------------------------------------------------------------

%prep
%setup -qn krunner-kopete-contacts-%{version}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT


