import http from 'k6/http';
import { check } from 'k6';

let baseUrl = __ENV.SERVICE_URL ? __ENV.SERVICE_URL : "http://localhost:8000"

export default function () {
    let payload = JSON.stringify({
        "requester": "djan",
        "message": "make it fast 🏎️",
    })

    let parameters = {
        'headers': {
            'Content-Type': 'application/json',
        },
    };

    const res = http.post(baseUrl + '/message', payload, parameters);
    check(res, { 'status was 200': (r) => r.status == 200 });
}
