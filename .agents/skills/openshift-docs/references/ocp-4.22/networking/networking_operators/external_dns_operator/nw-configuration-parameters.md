<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To customize the behavior of the External DNS Operator, configure the available parameters in the `ExternalDNS` custom resource (CR). By configuraing parameters, you can control how the Operator synchronizes services and routes with your external DNS provider.

# External DNS Operator configuration parameters

To customize the behavior of the External DNS Operator, configure the available parameters in the `ExternalDNS` custom resource (CR).

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>spec</code></p></td>
<td style="text-align: left;"><p>Enables the type of a cloud provider.</p>
<div class="sourceCode" id="cb1"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">spec</span><span class="kw">:</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">provider</span><span class="kw">:</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">type</span><span class="kw">:</span><span class="at"> AWS</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">aws</span><span class="kw">:</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="fu">credentials</span><span class="kw">:</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="at">        </span><span class="fu">name</span><span class="kw">:</span><span class="at"> aws-access-key</span></span></code></pre></div>
<ul>
<li><p><code>provider.type</code>: Specifies available options such as AWS, Google Cloud, Azure, and Infoblox.</p></li>
<li><p><code>provider.aws.credentials.name</code>: Specifies a secret name for your cloud provider.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>zones</code></p></td>
<td style="text-align: left;"><p>Enables you to specify DNS zones by their domains. If you do not specify zones, the <code>ExternalDNS</code> resource discovers all of the zones present in your cloud provider account.</p>
<div class="sourceCode" id="cb2"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">zones</span><span class="kw">:</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="kw">-</span><span class="at"> </span><span class="st">&quot;&lt;zone_id&gt;&quot;</span></span></code></pre></div>
<ul>
<li><p><code>&lt;zone_id&gt;</code>: Specifies the name of DNS zones.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>domains</code></p></td>
<td style="text-align: left;"><p>Enables you to specify AWS zones by their domains. If you do not specify domains, the <code>ExternalDNS</code> resource discovers all of the zones present in your cloud provider account.</p>
<div class="sourceCode" id="cb3"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="fu">domains</span><span class="kw">:</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a><span class="kw">-</span><span class="at"> </span><span class="fu">filterType</span><span class="kw">:</span><span class="at"> Include</span></span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">matchType</span><span class="kw">:</span><span class="at"> Exact</span></span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">name</span><span class="kw">:</span><span class="at"> </span><span class="st">&quot;myzonedomain1.com&quot;</span></span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a><span class="kw">-</span><span class="at"> </span><span class="fu">filterType</span><span class="kw">:</span><span class="at"> Include</span></span>
<span id="cb3-6"><a href="#cb3-6" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">matchType</span><span class="kw">:</span><span class="at"> Pattern</span></span>
<span id="cb3-7"><a href="#cb3-7" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">pattern</span><span class="kw">:</span><span class="at"> </span><span class="st">&quot;.*</span><span class="sc">\\</span><span class="st">.otherzonedomain</span><span class="sc">\\</span><span class="st">.com&quot;</span></span></code></pre></div>
<ul>
<li><p><code>domains.filterType</code>: Specifies that the <code>ExternalDNS</code> resource includes the domain name.</p></li>
<li><p><code>domains.matchType</code>: Specifies that the domain matching has to be exact as opposed to regular expression match.</p></li>
<li><p><code>domains.name</code>: Specifies the name of the domain.</p></li>
<li><p><code>filterType.matchType</code>: Specifies the <code>regex-domain-filter</code> flag in the <code>ExternalDNS</code> resource. You can limit possible domains by using a Regex filter.</p></li>
<li><p><code>filterType.pattern</code>: Specifies the regex pattern to be used by the <code>ExternalDNS</code> resource to filter the domains of the target zones.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>source</code></p></td>
<td style="text-align: left;"><p>Enables you to specify the source for the DNS records, <code>Service</code> or <code>Route</code>.</p>
<div class="sourceCode" id="cb4"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a><span class="fu">source</span><span class="kw">:</span></span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">type</span><span class="kw">:</span><span class="at"> Service</span></span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">service</span><span class="kw">:</span></span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">serviceType</span><span class="kw">:</span></span>
<span id="cb4-5"><a href="#cb4-5" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="kw">-</span><span class="at"> LoadBalancer</span></span>
<span id="cb4-6"><a href="#cb4-6" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="kw">-</span><span class="at"> ClusterIP</span></span>
<span id="cb4-7"><a href="#cb4-7" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">labelFilter</span><span class="kw">:</span></span>
<span id="cb4-8"><a href="#cb4-8" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">matchLabels</span><span class="kw">:</span></span>
<span id="cb4-9"><a href="#cb4-9" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="fu">external-dns.mydomain.org/publish</span><span class="kw">:</span><span class="at"> </span><span class="st">&quot;yes&quot;</span></span>
<span id="cb4-10"><a href="#cb4-10" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">hostnameAnnotation</span><span class="kw">:</span><span class="at"> </span><span class="st">&quot;Allow&quot;</span></span>
<span id="cb4-11"><a href="#cb4-11" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">fqdnTemplate</span><span class="kw">:</span></span>
<span id="cb4-12"><a href="#cb4-12" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="kw">-</span><span class="at"> </span><span class="st">&quot;{}.myzonedomain.com&quot;</span></span></code></pre></div>
<ul>
<li><p><code>source</code>: Specifies the settings for the source of DNS records.</p></li>
<li><p><code>source.type</code>: Specifies that the <code>ExternalDNS</code> CR uses the <code>Service</code> type as the source for creating DNS records.</p></li>
<li><p><code>service.serviceType</code>: Specifies the <code>service-type-filter</code> flag in the <code>ExternalDNS</code> resource. The <code>serviceType</code> contains the following fields: <code>default</code>: <code>LoadBalancer</code>; <code>expected</code>: <code>ClusterIP</code>; <code>NodePort</code>; <code>LoadBalancer</code>; <code>ExternalName</code>.</p></li>
<li><p><code>service.labelFilter</code>: Specifies that the controller considers only those resources that match with label filter.</p></li>
<li><p><code>hostnameAnnotation</code>: Specifies that the default value for <code>hostnameAnnotation</code> is <code>Ignore</code> which instructs <code>ExternalDNS</code> to generate DNS records by using the templates specified in the field <code>fqdnTemplates</code>. When the value is <code>Allow</code> the DNS records get generated based on the value specified in the <code>external-dns.alpha.kubernetes.io/hostname</code> annotation.</p></li>
<li><p><code>fqdnTemplate</code>: Specifies that the External DNS Operator uses a string to generate DNS names from sources that do not define a hostname, or to add a hostname suffix when paired with the fake source.</p></li>
</ul>
<div class="sourceCode" id="cb5"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb5-1"><a href="#cb5-1" aria-hidden="true" tabindex="-1"></a><span class="fu">source</span><span class="kw">:</span></span>
<span id="cb5-2"><a href="#cb5-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">type</span><span class="kw">:</span><span class="at"> OpenShiftRoute</span></span>
<span id="cb5-3"><a href="#cb5-3" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">openshiftRouteOptions</span><span class="kw">:</span></span>
<span id="cb5-4"><a href="#cb5-4" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">routerName</span><span class="kw">:</span><span class="at"> default</span></span>
<span id="cb5-5"><a href="#cb5-5" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">labelFilter</span><span class="kw">:</span></span>
<span id="cb5-6"><a href="#cb5-6" aria-hidden="true" tabindex="-1"></a><span class="at">      </span><span class="fu">matchLabels</span><span class="kw">:</span></span>
<span id="cb5-7"><a href="#cb5-7" aria-hidden="true" tabindex="-1"></a><span class="at">        </span><span class="fu">external-dns.mydomain.org/publish</span><span class="kw">:</span><span class="at"> </span><span class="st">&quot;yes&quot;</span></span></code></pre></div>
<ul>
<li><p><code>source.type</code>: Specifies the creation of DNS records.</p></li>
<li><p><code>openshiftRouteOptions.routerName</code>: Specifies if the source type is <code>OpenShiftRoute</code>. If so, you can pass the Ingress Controller name. The <code>ExternalDNS</code> resource uses the canonical name of the Ingress Controller as the target for CNAME records.</p></li>
</ul></td>
</tr>
</tbody>
</table>
