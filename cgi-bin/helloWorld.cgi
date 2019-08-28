#!/bin/sh

exec "$COMMANDER_HOME/bin/ec-perl" -x "$0" "${@}"

#!perl

use strict;
use ElectricCommander;
use CGI;

$| = 1;

# Create a single instance of the Perl access to ElectricCommander
my $ec = new ElectricCommander();

use Data::Dumper;

print "Content-type: text/html\n\n";

my $ref = $ENV{HTTP_REFERER};

print "$ref\n";

use LWP::UserAgent;
my $ua = LWP::UserAgent->new;

my $ref_uri = URI->new($ref);
print Dumper $ref_uri;

my %query_form = $ref_uri->query_form;
print Dumper \%query_form;
use URI::Escape;

my $code = $query_form{code};

print "Code\n";
print Dumper $code;

my $redirect_uri = uri_escape('https://vivarium2/commander/pages/TestCGIPlugin/helloworld_run');

my $request_codes_url = URI->new("https://ven01734.service-now.com/oauth_auth.do?grant_type=authorization_code&code=$code&redirect_uri=$redirect_uri&client_id=a22985e94027b30096e46d463da05698&client_secret=test");

print Dumper $request_codes_url;

my $response = $ua->get($request_codes_url);

print "<pre>";

print Dumper $response;


# https://ven01734.service-now.com/oauth_token.do?grant_type=code&code=k8z2SbFCe7pCNm1ApCyVcXnFj-uIb--zFzTXDl8-F3T0Z0ojQDOnTFvQThHIn6QNehXBENtOCKOiuf9tXy_7tw&redirect_uri=https://vivarium2/commander/pages/TestCGIPlugin/helloworld_run&client_id=a22985e94027b30096e46d463da05698


print "Hello World!";
print Dumper \%ENV;


print "</pre>";
