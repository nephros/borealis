# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       borealis-sound-theme

# >> macros
# << macros
%define themename borealis
%define themedir %{_datadir}/sounds/%{themename}
%define stereodir %{themedir}/stereo

Summary:    Boralis Sound Theme by Ivica Ico Bukvic
Version:    0.9a
Release:    1
Group:      Amusements
License:    Artistic 2.0
BuildArch:  noarch
URL:        http://ico.bukvic.net/main/borealis/
Source0:    %{name}-%{version}.tar.gz
Source100:  borealis-sound-theme.yaml
Requires(post): systemd
Requires(postun): systemd

%description
Popular KDE sound theme Borealis by Ivica Ico Bukvic packaged for Sailfish OS.

Ivica writes:

Back in 2004 I composed a sound theme for the KDE desktop environment
and posted it on now defunct kde-look.org. Borealis soon became the top
rated theme and to this day remains one of the top themes with the
largest (~300K) number of downloads. Over the years, components of the
theme were licensed for a number of projects including Gnome and Ubuntu
Studio. In 2008, the theme also served as the foundation for a
commission from the now defunct SUN Microsystems Inc. where I was
tasked to design a collection of sound themes for the (now also
defunct) Open Solaris project.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre


make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%post
# >> post
%systemd_user_post restart ambienced
# << post

%postun
# >> postun
%systemd_user_postun restart ambienced
# << postun

%files
%defattr(-,root,root,-)
%doc README
%dir %{themedir}
%{themedir}/index.theme
%{themedir}/stereo.index
%dir %{stereodir}
%{stereodir}/*.ogg
# >> files
# << files
