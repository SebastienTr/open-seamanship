// Checks the dashboard's rule-of-twelfths maths: node tests/js/tide_test.js dashboard/dashboard.js
const fs=require('fs'); const src=fs.readFileSync(process.argv[2],'utf8');
const body=src.slice(src.indexOf('  var CUM'), src.indexOf("  ['t-lwt',"));
const vals={}; const outs={};
const $=id=>({get value(){return vals[id]}, set textContent(v){outs[id]=v}});
const pad=n=>(n<10?'0':'')+n;
const tide=new Function('$','pad', body+'; return tide;')($,pad);
function run(lwt,lwh,hwt,hwh,at){Object.assign(vals,{'t-lwt':lwt,'t-lwh':String(lwh),'t-hwt':hwt,'t-hwh':String(hwh),'t-at':at}); tide(); return outs['t-out'];}
const cases=[
 ['06:00',0.8,'12:00',5.0,'06:00','0.8','rising'],['06:00',0.8,'12:00',5.0,'07:00','1.2','rising'],
 ['06:00',0.8,'12:00',5.0,'08:00','1.9'],['06:00',0.8,'12:00',5.0,'09:00','2.9'],['06:00',0.8,'12:00',5.0,'12:00','5.0'],
 ['06:00',0.8,'12:00',5.0,'13:00','4.6','falling'],['06:00',0.8,'12:00',5.0,'15:00','2.9','falling'],['06:00',0.8,'12:00',5.0,'18:00','0.8'],
 ['12:00',0.8,'06:00',5.0,'09:00','2.9','falling'],['12:00',0.8,'06:00',5.0,'14:00','1.8','rising'],
 ['22:00',1.0,'04:00',4.0,'01:00','2.5'],['22:00',1.0,'04:00',4.0,'23:00','1.3','rising'],
];
// LW 22:00 then HW 04:00 crosses midnight.
let fail=0; for(const c of cases){const r=run(...c.slice(0,5)); const ok=r.includes('About '+c[5]+' m')&&(!c[6]||r.includes(c[6])); if(!ok)fail++; if(!ok)console.log('FAIL', c.slice(0,5).join(' '), '->', r);}
console.log('tide: '+(cases.length-fail)+'/'+cases.length+' ok'); process.exit(fail?1:0);
