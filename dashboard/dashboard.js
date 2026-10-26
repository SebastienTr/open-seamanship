/* Open Seamanship dashboard. Plain JavaScript, no network beyond this N.O.M.A.D. */
(function () {
  'use strict';

  var CFG = window.OSP_CONFIG || {};
  var KIWIX_PORT = CFG.kiwixPort || '8090';
  var KIWIX_PUBLIC = CFG.kiwixPublicUrl || (location.protocol + '//' + location.hostname + ':' + KIWIX_PORT);
  var PACK_BOOK_PREFIX = 'open-seamanship';

  function $(id) { return document.getElementById(id); }
  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }
  function store(key, value) {
    try {
      if (value === undefined) return window.localStorage.getItem(key);
      window.localStorage.setItem(key, value);
    } catch (e) { return null; }
    return null;
  }

  /* ---- display mode ---------------------------------------------------- */
  function setTheme(name) {
    document.documentElement.setAttribute('data-theme', name);
    store('osp-theme', name);
    var buttons = document.querySelectorAll('.themes button');
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].setAttribute('aria-pressed', buttons[i].getAttribute('data-theme') === name ? 'true' : 'false');
    }
  }
  var saved = store('osp-theme');
  setTheme(saved || (window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches ? 'dusk' : 'day'));
  document.querySelector('.themes').addEventListener('click', function (ev) {
    var t = ev.target.getAttribute && ev.target.getAttribute('data-theme');
    if (t) setTheme(t);
  });

  /* ---- clocks ------------------------------------------------------------ */
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function tick() {
    var d = new Date();
    $('utc').textContent = pad(d.getUTCHours()) + ':' + pad(d.getUTCMinutes());
    $('local').textContent = pad(d.getHours()) + ':' + pad(d.getMinutes());
  }
  tick();
  setInterval(tick, 15000);

  /* ---- pack sections ----------------------------------------------------- */
  function loadSections() {
    fetch('sections.json').then(function (r) { return r.json(); }).then(function (data) {
      $('version').textContent = data.version || '';
      var ul = $('sections');
      data.sections.forEach(function (s) {
        var li = el('li', 'tile' + (s.accent ? ' accent' : '') + (s.count ? '' : ' empty'));
        var a = el('a');
        a.href = 'pack/' + s.slug + '/index.html';
        a.appendChild(el('span', 't', s.title));
        a.appendChild(el('span', 'd', s.blurb));
        var unit = s.slug === 'library' ? ' document' : ' page';
        a.appendChild(el('span', 'n', s.count ? s.count + unit + (s.count > 1 ? 's' : '') : 'Being written'));
        li.appendChild(a);
        ul.appendChild(li);
      });
    }).catch(function () {
      $('sections').appendChild(el('li', 'tile muted', 'Pack index missing from this image.'));
    });
  }

  /* ---- Kiwix libraries ---------------------------------------------------- */
  var books = [];   // {name, title, path, mariner}

  function parseCatalog(xml) {
    var doc = new DOMParser().parseFromString(xml, 'application/xml');
    var entries = doc.getElementsByTagName('entry');
    var out = [];
    for (var i = 0; i < entries.length; i++) {
      var e = entries[i];
      var name = text(e, 'name');
      var id = text(e, 'id').replace(/^urn:uuid:/, '');
      var path = null;
      var links = e.getElementsByTagName('link');
      for (var j = 0; j < links.length; j++) {
        if (links[j].getAttribute('type') === 'text/html') path = links[j].getAttribute('href');
      }
      if (name && id && path) {
        out.push({
          id: id, name: name, title: text(e, 'title') || name, path: path,
          content: path.replace(/^.*\/content\//, '').replace(/\/.*$/, ''),   // kiwix-serve book path name
          mariner: name.indexOf(PACK_BOOK_PREFIX) === 0
        });
      }
    }
    return out;
  }
  function text(node, tag) {
    var n = node.getElementsByTagName(tag)[0];
    return n ? n.textContent : '';
  }

  function describe(b) {
    if (b.name === 'open-seamanship-private') return 'Your private shelf: engine manuals and notes. Not for sharing.';
    if (b.name.indexOf('open-seamanship_') === 0) return 'The Open Seamanship pack with its library of manuals, as a Kiwix library.';
    if (b.name.indexOf('open-seamanship-wiki_') === 0) return 'Local Wikipedia shelf: coasts, harbours, lights, history.';
    return 'Kiwix library';
  }

  function loadLibraries() {
    fetch('kiwix/catalog/v2/entries?count=-1').then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.text();
    }).then(function (xml) {
      books = parseCatalog(xml);
      renderLibraries();
      renderScope();
    }).catch(function () {
      var ul = $('libraries');
      ul.innerHTML = '';
      var li = el('li', 'tile muted');
      li.appendChild(el('span', 't', 'Kiwix is not reachable'));
      li.appendChild(el('span', 'd', 'Start the Information Library from the N.O.M.A.D. Command Center, then reload this page.'));
      ul.appendChild(li);
      $('search-scope').textContent = 'Search needs Kiwix.';
    });
  }

  function renderLibraries() {
    var ul = $('libraries');
    ul.innerHTML = '';
    var mariner = books.filter(function (b) { return b.mariner; });
    mariner.sort(function (a, b) { return a.name < b.name ? -1 : 1; });
    mariner.forEach(function (b) {
      var li = el('li', 'tile' + (b.name === 'open-seamanship-private' ? ' private' : ''));
      var a = el('a');
      a.href = KIWIX_PUBLIC + b.path;
      a.appendChild(el('span', 't', b.title));
      a.appendChild(el('span', 'd', describe(b)));
      li.appendChild(a);
      ul.appendChild(li);
    });
    if (!books.some(function (b) { return b.name === 'open-seamanship-private'; })) {
      var li = el('li', 'tile muted');
      li.appendChild(el('span', 't', 'No private shelf yet'));
      li.appendChild(el('span', 'd', 'On the N.O.M.A.D. host: make fetch-private, make private, then install it (see the README).'));
      ul.appendChild(li);
    }
    var all = el('li', 'tile');
    var a = el('a');
    a.href = KIWIX_PUBLIC + '/';
    a.appendChild(el('span', 't', 'All Kiwix libraries'));
    a.appendChild(el('span', 'd', books.length + ' librar' + (books.length === 1 ? 'y' : 'ies') + ' on this N.O.M.A.D.: Wikipedia, medicine, repair…'));
    all.appendChild(a);
    ul.appendChild(all);
  }

  function searchBooks() {
    var mariner = books.filter(function (b) { return b.mariner; });
    return mariner.length ? mariner : [];
  }
  function renderScope() {
    var m = searchBooks();
    $('search-scope').textContent = m.length
      ? 'Searching ' + m.map(function (b) { return b.title; }).join(', ') + '. PDF manuals are found by their title.'
      : 'No mariner library in Kiwix yet: install the Open Seamanship ZIM to search it.';
  }

  /* ---- search ------------------------------------------------------------- */
  // Per book, two Kiwix calls: title suggestions (finds PDF manuals, which have no full text)
  // and full-text search. Books are searched one by one so one broken index does not fail all.
  function getText(url) {
    return fetch(url).then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.text(); });
  }
  function titleHits(b, q) {
    return getText('kiwix/suggest?content=' + encodeURIComponent(b.content) + '&term=' + encodeURIComponent(q) + '&count=8')
      .then(function (t) {
        return JSON.parse(t).filter(function (x) { return x.kind === 'path'; }).map(function (x) {
          return { title: x.value, link: '/content/' + b.content + '/' + x.path, book: b.title, desc: '' };
        });
      }).catch(function () { return []; });
  }
  function fullTextHits(b, q) {
    var params = 'pattern=' + encodeURIComponent(q) + '&format=xml&pageLength=25&books.id=' + encodeURIComponent(b.id);
    return getText('kiwix/search?' + params).then(function (xml) {
      var doc = new DOMParser().parseFromString(xml, 'application/xml');
      var items = doc.getElementsByTagName('item');
      var out = [];
      for (var i = 0; i < items.length; i++) {
        var it = items[i], bk = it.getElementsByTagName('book')[0];
        out.push({ title: text(it, 'title'), link: text(it, 'link'), book: bk ? text(bk, 'title') : '', desc: text(it, 'description') });
      }
      return out;
    }).catch(function () { return null; });
  }
  function plainWithBold(html) {
    // Kiwix marks matches with <b>; keep only that, as text nodes and <b> elements.
    var tmp = new DOMParser().parseFromString('<p>' + html + '</p>', 'text/html').body.firstChild;
    var p = el('p');
    (function walk(node, into) {
      for (var c = node.firstChild; c; c = c.nextSibling) {
        if (c.nodeType === 3) into.appendChild(document.createTextNode(c.textContent));
        else if (c.nodeName === 'B') into.appendChild(el('b', null, c.textContent));
        else walk(c, into);
      }
    })(tmp, p);
    return p;
  }

  $('search-form').addEventListener('submit', function (ev) {
    ev.preventDefault();
    var q = $('q').value.trim();
    var out = $('results');
    out.innerHTML = '';
    if (!q) return;
    var scope = searchBooks();
    if (!scope.length) {
      out.appendChild(el('p', 'scope', 'Nothing to search yet.'));
      return;
    }
    out.appendChild(el('p', 'scope', 'Searching…'));
    Promise.all([
      Promise.all(scope.map(function (b) { return titleHits(b, q); })),
      Promise.all(scope.map(function (b) { return fullTextHits(b, q); }))
    ]).then(function (res) {
      var full = res[1].filter(function (r) { return r !== null; });
      var failed = !full.length;   // every full-text call failed: Kiwix is probably down
      var seen = {}, hits = [];
      [].concat.apply([], res[0]).concat([].concat.apply([], full)).forEach(function (h) {
        if (seen[h.link]) return;
        seen[h.link] = true;
        hits.push(h);
      });
      out.innerHTML = '';
      if (!hits.length) {
        out.appendChild(el('p', 'scope', failed ? 'Search failed: is Kiwix running?' : 'No result for «' + q + '». Try fewer or simpler words.'));
        return;
      }
      var ol = el('ol', 'hits');
      hits.forEach(function (h) {
        var li = el('li');
        var a = el('a', null, h.title);
        a.href = KIWIX_PUBLIC + h.link;
        li.appendChild(a);
        if (h.book) li.appendChild(el('span', 'src', h.book));
        if (h.desc) li.appendChild(plainWithBold(h.desc));
        ol.appendChild(li);
      });
      out.appendChild(ol);
    });
  });

  /* ---- rescan -------------------------------------------------------------- */
  $('rescan').addEventListener('click', function () {
    var msg = $('rescan-msg');
    msg.textContent = 'Rescanning…';
    fetch('nomad/api/zim/rescan-library', { method: 'POST' }).then(function (r) {
      return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; });
    }).then(function (res) {
      if (!res.ok) throw new Error();
      var added = res.j && res.j.added != null ? res.j.added : (res.j && res.j.data && res.j.data.added);
      msg.textContent = 'Done' + (added != null ? ': ' + added + ' new librar' + (added === 1 ? 'y' : 'ies') : '') + '.';
      setTimeout(loadLibraries, 1500);
    }).catch(function () {
      msg.textContent = 'Could not reach N.O.M.A.D. Use Content Manager → Rescan Library instead.';
    });
  });

  /* ---- converter ------------------------------------------------------------- */
  var CONV = [
    ['kn → km/h', function (v) { return v * 1.852; }, 'km/h'],
    ['kn → m/s', function (v) { return v * 0.514444; }, 'm/s'],
    ['km/h → kn', function (v) { return v / 1.852; }, 'kn'],
    ['nautical miles → km', function (v) { return v * 1.852; }, 'km'],
    ['km → nautical miles', function (v) { return v / 1.852; }, 'NM'],
    ['m → ft', function (v) { return v * 3.28084; }, 'ft'],
    ['ft → m', function (v) { return v * 0.3048; }, 'm'],
    ['fathoms → m', function (v) { return v * 1.8288; }, 'm'],
    ['hp → kW', function (v) { return v * 0.745700; }, 'kW'],
    ['kW → hp', function (v) { return v / 0.745700; }, 'hp'],
    ['bar → psi', function (v) { return v * 14.5038; }, 'psi'],
    ['psi → bar', function (v) { return v / 14.5038; }, 'bar'],
    ['°C → °F', function (v) { return v * 9 / 5 + 32; }, '°F'],
    ['°F → °C', function (v) { return (v - 32) * 5 / 9; }, '°C'],
    ['L → US gal', function (v) { return v / 3.785411784; }, 'US gal'],
    ['US gal → L', function (v) { return v * 3.785411784; }, 'L'],
    ['imperial gal → L', function (v) { return v * 4.54609; }, 'L'],
    ['N·m → lbf·ft', function (v) { return v * 0.737562; }, 'lbf·ft'],
    ['lbf·ft → N·m', function (v) { return v / 0.737562; }, 'N·m']
  ];
  var kind = $('cv-kind');
  CONV.forEach(function (c, i) { var o = el('option', null, c[0]); o.value = i; kind.appendChild(o); });
  function round(x) { return Math.abs(x) >= 100 ? x.toFixed(0) : Math.abs(x) >= 10 ? x.toFixed(1) : x.toFixed(2); }
  function convert() {
    var v = parseFloat($('cv-in').value);
    var c = CONV[kind.value];
    $('cv-out').textContent = isNaN(v) ? '' : '= ' + round(c[1](v)) + ' ' + c[2];
  }
  $('cv-in').addEventListener('input', convert);
  kind.addEventListener('change', convert);
  convert();

  /* ---- fuel and range --------------------------------------------------------- */
  function fuel() {
    var f = parseFloat($('f-fuel').value), r = parseFloat($('f-rate').value);
    var s = parseFloat($('f-speed').value), res = parseFloat($('f-res').value) || 0;
    if (!(f > 0 && r > 0)) { $('f-out').textContent = ''; return; }
    var usable = f * (1 - Math.min(Math.max(res, 0), 100) / 100);
    var hours = usable / r;
    var h = Math.floor(hours), m = Math.round((hours - h) * 60);
    if (m === 60) { h += 1; m = 0; }
    var txt = usable.toFixed(1) + ' L usable: ' + h + ' h ' + pad(m) + ' min of running';
    if (s > 0) txt += ', about ' + (hours * s).toFixed(0) + ' NM at ' + s + ' kn';
    $('f-out').textContent = txt + '.';
  }
  ['f-fuel', 'f-rate', 'f-speed', 'f-res'].forEach(function (id) { $(id).addEventListener('input', fuel); });
  fuel();

  /* ---- rule of twelfths -------------------------------------------------------- */
  var CUM = [0, 1, 3, 6, 9, 11, 12];   // twelfths of the range after each sixth of the duration
  function minutes(v) { var p = v.split(':'); return parseInt(p[0], 10) * 60 + parseInt(p[1], 10); }
  function tide() {
    var out = $('t-out');
    var lwt = $('t-lwt').value, hwt = $('t-hwt').value, at = $('t-at').value;
    var lwh = parseFloat($('t-lwh').value), hwh = parseFloat($('t-hwh').value);
    if (!lwt || !hwt || !at || isNaN(lwh) || isNaN(hwh)) { out.textContent = ''; return; }
    var a = minutes(lwt), b = minutes(hwt), t = minutes(at);
    // The two tides given make one half tide (LW then HW, or HW then LW, possibly across
    // midnight). The estimate covers it and the next half tide, assumed to last as long.
    var d = b - a;
    if (d > 720) d -= 1440;
    if (d < -720) d += 1440;
    var risingFirst = d > 0;
    var first = risingFirst ? a : b, dur = Math.abs(d);
    if (dur < 180 || dur > 540) { out.textContent = 'Low and high water should be 3 to 9 hours apart.'; return; }
    var x = ((t - first + 1440) % 1440) / dur;                     // 0..1 first half tide, 1..2 the next one
    if (x > 2) { out.textContent = 'Too far from these tides: enter the tides around that time.'; return; }
    var rising = x <= 1 ? risingFirst : !risingFirst;
    var f = (x <= 1 ? x : x - 1) * 6;              // in "tide hours"
    var i = Math.min(Math.floor(f), 5);
    var cum = CUM[i] + (CUM[i + 1] - CUM[i]) * (f - i);
    var lo = Math.min(lwh, hwh), range = Math.abs(hwh - lwh);
    var h = rising ? lo + range * cum / 12 : lo + range - range * cum / 12;
    out.textContent = 'About ' + h.toFixed(1) + ' m above chart datum (' + (rising ? 'rising' : 'falling') +
      ', range ' + range.toFixed(1) + ' m).';
  }
  ['t-lwt', 't-lwh', 't-hwt', 't-hwh', 't-at'].forEach(function (id) { $(id).addEventListener('input', tide); });
  tide();

  /* ---- Beaufort ------------------------------------------------------------------ */
  var BF = [
    [0, '< 1', 'Calm', 'Like a mirror'],
    [1, '1–3', 'Light air', 'Ripples, ~0.1 m'],
    [2, '4–6', 'Light breeze', 'Small wavelets, ~0.2 m'],
    [3, '7–10', 'Gentle breeze', 'Large wavelets, ~0.6 m'],
    [4, '11–16', 'Moderate breeze', 'Small waves, frequent white horses, ~1 m'],
    [5, '17–21', 'Fresh breeze', 'Moderate waves, many white horses, ~2 m'],
    [6, '22–27', 'Strong breeze', 'Large waves, white foam crests, ~3 m'],
    [7, '28–33', 'Near gale', 'Sea heaps up, foam in streaks, ~4 m'],
    [8, '34–40', 'Gale', 'Moderately high waves, crests break into spindrift, ~5.5 m'],
    [9, '41–47', 'Strong gale', 'High waves, dense foam, spray, ~7 m'],
    [10, '48–55', 'Storm', 'Very high waves, sea white, ~9 m'],
    [11, '56–63', 'Violent storm', 'Exceptionally high waves, ~11.5 m'],
    [12, '≥ 64', 'Hurricane', 'Air full of foam and spray, 14 m and more']
  ];
  var tb = $('bf-body');
  BF.forEach(function (r) {
    var tr = el('tr', r[0] >= 7 ? 'warn' : null);
    r.forEach(function (c) { tr.appendChild(el('td', null, String(c))); });
    tb.appendChild(tr);
  });

  loadSections();
  loadLibraries();
})();
