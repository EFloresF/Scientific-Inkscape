#!/usr/bin/env python
# coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: full11 data
# Created: 15.10.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

from svgwrite.data.types import SVGAttribute, SVGMultiAttribute
from svgwrite.data.types import SVGElement
from svgwrite.data.typechecker import Full11TypeChecker as TypeChecker

empty_list = []

attributes = {
    "accent-height": SVGAttribute(
        "accent-height", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "accumulate": SVGAttribute(
        "accumulate", anim=False, types=empty_list, const=frozenset(["none", "sum"])
    ),
    "additive": SVGAttribute(
        "additive", anim=False, types=empty_list, const=frozenset(["sum", "replace"])
    ),
    "alignment-baseline": SVGAttribute(
        "alignment-baseline",
        anim=True,
        types=empty_list,
        const=frozenset(
            [
                "mathematical",
                "before-edge",
                "central",
                "baseline",
                "auto",
                "hanging",
                "ideographic",
                "inherit",
                "middle",
                "alphabetic",
                "text-before-edge",
                "text-after-edge",
                "after-edge",
            ]
        ),
    ),
    "alphabetic": SVGAttribute(
        "alphabetic", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "amplitude": SVGAttribute(
        "amplitude", anim=True, types=frozenset(["number"]), const=empty_list
    ),
    "arabic-form": SVGAttribute(
        "arabic-form",
        anim=False,
        types=empty_list,
        const=frozenset(["terminal", "initial", "isolated", "medial"]),
    ),
    "ascent": SVGAttribute(
        "ascent", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "attributeName": SVGAttribute(
        "attributeName", anim=False, types=frozenset(["name"]), const=empty_list
    ),
    "attributeType": SVGAttribute(
        "attributeType",
        anim=False,
        types=empty_list,
        const=frozenset(["XML", "auto", "CSS"]),
    ),
    "azimuth": SVGAttribute(
        "azimuth", anim=True, types=frozenset(["number"]), const=empty_list
    ),
    "baseFrequency": SVGAttribute(
        "baseFrequency",
        anim=True,
        types=frozenset(["number-optional-number"]),
        const=empty_list,
    ),
    "baseline-shift": SVGAttribute(
        "baseline-shift",
        anim=True,
        types=frozenset(["percentage", "length"]),
        const=frozenset(["super", "baseline", "inherit", "sub"]),
    ),
    "baseProfile": SVGAttribute(
        "baseProfile",
        anim=False,
        types=empty_list,
        const=frozenset(["full", "tiny", "basic", "none"]),
    ),
    "bbox": SVGAttribute(
        "bbox", anim=False, types=frozenset(["string"]), const=empty_list
    ),
    "begin": SVGAttribute(
        "begin",
        anim=True,
        types=frozenset(["timing-value-list"]),
        const=frozenset(["indefinite"]),
    ),
    "bias": SVGAttribute(
        "bias", anim=True, types=frozenset(["number"]), const=empty_list
    ),
    "by": SVGAttribute("by", anim=False, types=frozenset(["string"]), const=empty_list),
    "calcMode": SVGAttribute(
        "calcMode",
        anim=False,
        types=empty_list,
        const=frozenset(["discrete", "linear", "paced", "spline"]),
    ),
    "cap-height": SVGAttribute(
        "cap-height", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "class": SVGAttribute(
        "class", anim=True, types=frozenset(["list-of-name"]), const=empty_list
    ),
    "clip": SVGAttribute(
        "clip",
        anim=True,
        types=frozenset(["shape"]),
        const=frozenset(["auto", "inherit"]),
    ),
    "clip-path": SVGAttribute(
        "clip-path",
        anim=True,
        types=frozenset(["IRI"]),
        const=frozenset(["none", "inherit"]),
    ),
    "clip-rule": SVGAttribute(
        "clip-rule",
        anim=True,
        types=empty_list,
        const=frozenset(["nonzero", "evenodd", "inherit"]),
    ),
    "clipPathUnits": SVGAttribute(
        "clipPathUnits",
        anim=True,
        types=empty_list,
        const=frozenset(["userSpaceOnUse", "objectBoundingBox"]),
    ),
    "color": SVGAttribute(
        "color", anim=True, types=frozenset(["color"]), const=frozenset(["inherit"])
    ),
    "color-interpolation": SVGAttribute(
        "color-interpolation",
        anim=True,
        types=empty_list,
        const=frozenset(["auto", "sRGB", "inherit", "linearRGB"]),
    ),
    "color-interpolation-filters": SVGAttribute(
        "color-interpolation-filters",
        anim=True,
        types=empty_list,
        const=frozenset(["auto", "sRGB", "inherit", "linearRGB"]),
    ),
    "color-profile": SVGAttribute(
        "color-profile",
        anim=True,
        types=frozenset(["FuncIRI", "name"]),
        const=frozenset(["auto", "sRGB", "inherit"]),
    ),
    "color-rendering": SVGAttribute(
        "color-rendering",
        anim=True,
        types=empty_list,
        const=frozenset(["auto", "optimizeQuality", "optimizeSpeed", "inherit"]),
    ),
    "contentScriptType": SVGAttribute(
        "contentScriptType", anim=True, types=frozenset(["string"]), const=empty_list
    ),
    "contentStyleType": SVGAttribute(
        "contentStyleType", anim=True, types=frozenset(["string"]), const=empty_list
    ),
    "cursor": SVGAttribute(
        "cursor",
        anim=True,
        types=frozenset(["list-of-FuncIRI"]),
        const=frozenset(
            [
                "sw-resize",
                "n-resize",
                "help",
                "text",
                "move",
                "auto",
                "w-resize",
                "pointer",
                "wait",
                "s-resize",
                "e-resize",
                "default",
                "inherit",
                "nw-resize",
                "ne-resize",
                "crosshair",
                "se-resize",
            ]
        ),
    ),
    "cx": SVGAttribute(
        "cx", anim=True, types=frozenset(["coordinate"]), const=empty_list
    ),
    "cy": SVGAttribute(
        "cy", anim=True, types=frozenset(["coordinate"]), const=empty_list
    ),
    "d": SVGMultiAttribute(
        {
            "* path": SVGAttribute(  # '*' means default attribute
                "d", anim=True, types=frozenset(["path-data"]), const=empty_list
            ),
            "glyph missing-glyph": SVGAttribute(
                "d", anim=False, types=frozenset(["path-data"]), const=empty_list
            ),
        }
    ),
    "descent": SVGAttribute(
        "descent", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "diffuseConstant": SVGAttribute(
        "diffuseConstant", anim=True, types=frozenset(["number"]), const=empty_list
    ),
    "direction": SVGAttribute(
        "direction",
        anim=False,
        types=empty_list,
        const=frozenset(["ltr", "inherit", "rtl"]),
    ),
    "display": SVGAttribute(
        "display",
        anim=True,
        types=empty_list,
        const=frozenset(
            [
                "inline-table",
                "table-header-group",
                "table-footer-group",
                "none",
                "table-row",
                "table-caption",
                "table-column",
                "marker",
                "table",
                "compact",
                "table-row-group",
                "run-in",
                "inherit",
                "list-item",
                "table-cell",
                "inline",
                "block",
                "table-column-group",
            ]
        ),
    ),
    "divisor": SVGAttribute(
        "divisor", anim=True, types=frozenset(["number"]), const=empty_list
    ),
    "dominant-baseline": SVGAttribute(
        "dominant-baseline",
        anim=True,
        types=empty_list,
        const=frozenset(
            [
                "mathematical",
                "use-script",
                "ideographic",
                "central",
                "reset-size",
                "auto",
                "hanging",
                "inherit",
                "middle",
                "alphabetic",
                "text-before-edge",
                "text-after-edge",
                "no-change",
            ]
        ),
    ),
    "dur": SVGAttribute(
        "dur",
        anim=True,
        types=frozenset(["time"]),
        const=frozenset(["media", "indefinite"]),
    ),
    "dx": SVGMultiAttribute(
        {
            "* altGlyph text tref tspan": SVGAttribute(
                "dx", anim=True, types=frozenset(["list-of-length"]), const=empty_list
            ),
            "feOffset": SVGAttribute(
                "dx", anim=True, types=frozenset(["number"]), const=empty_list
            ),
            "glyphRef": SVGAttribute(
                "dx", anim=False, types=frozenset(["number"]), const=empty_list
            ),
        }
    ),
    "dy": SVGMultiAttribute(
        {
            "* altGlyph text tref tspan": SVGAttribute(
                "dy", anim=True, types=frozenset(["list-of-length"]), const=empty_list
            ),
            "feOffset": SVGAttribute(
                "dy", anim=True, types=frozenset(["number"]), const=empty_list
            ),
            "glyphRef": SVGAttribute(
                "dy", anim=False, types=frozenset(["number"]), const=empty_list
            ),
        }
    ),
    "edgeMode": SVGAttribute(
        "edgeMode",
        anim=True,
        types=empty_list,
        const=frozenset(["wrap", "duplicate", "none"]),
    ),
    "elevation": SVGAttribute(
        "elevation", anim=True, types=frozenset(["number"]), const=empty_list
    ),
    "enable-background": SVGAttribute(
        "enable-background",
        anim=True,
        types=frozenset(["string"]),
        const=frozenset(["accummulate", "new", "inherit"]),
    ),
    "end": SVGAttribute(
        "end",
        anim=False,
        types=frozenset(["timing-value-list"]),
        const=frozenset(["indefinite"]),
    ),
    "exponent": SVGAttribute(
        "exponent", anim=True, types=frozenset(["number"]), const=empty_list
    ),
    "externalResourcesRequired": SVGAttribute(
        "externalResourcesRequired",
        anim=True,
        types=empty_list,
        const=frozenset(["true", "false"]),
    ),
    "fill": SVGMultiAttribute(
        {
            "*": SVGAttribute(
                "fill", anim=True, types=frozenset(["paint"]), const=empty_list
            ),
            "set animateMotion animate animateColor animateTransform": SVGAttribute(
                "fill",
                anim=False,
                types=empty_list,
                const=frozenset(["freeze", "remove"]),
            ),
        }
    ),
    "fill-opacity": SVGAttribute(
        "fill-opacity",
        anim=True,
        types=frozenset(["number"]),
        const=frozenset(["inherit"]),
    ),
    "fill-rule": SVGAttribute(
        "fill-rule",
        anim=True,
        types=empty_list,
        const=frozenset(["nonzero", "evenodd", "inherit"]),
    ),
    "filter": SVGAttribute(
        "filter",
        anim=True,
        types=frozenset(["FuncIRI"]),
        const=frozenset(["none", "inherit"]),
    ),
    "filterRes": SVGAttribute(
        "filterRes",
        anim=True,
        types=frozenset(["number-optional-number"]),
        const=empty_list,
    ),
    "filterUnits": SVGAttribute(
        "filterUnits",
        anim=True,
        types=empty_list,
        const=frozenset(["userSpaceOnUse", "objectBoundingBox"]),
    ),
    "flood-color": SVGAttribute(
        "flood-color",
        anim=True,
        types=frozenset(["color", "icccolor"]),
        const=frozenset(["currentColor", "inherit"]),
    ),
    "flood-opacity": SVGAttribute(
        "flood-opacity",
        anim=True,
        types=frozenset(["number"]),
        const=frozenset(["inherit"]),
    ),
    "font": SVGAttribute(
        "font", anim=True, types=frozenset(["string"]), const=empty_list
    ),
    "font-family": SVGAttribute(
        "font-family", anim=False, types=frozenset(["string"]), const=empty_list
    ),
    "font-size": SVGAttribute(
        "font-size",
        anim=False,
        types=frozenset(["length"]),
        const=frozenset(["inherit"]),
    ),
    "font-size-adjust": SVGAttribute(
        "font-size-adjust",
        anim=True,
        types=frozenset(["number"]),
        const=frozenset(["none", "inherit"]),
    ),
    "font-stretch": SVGAttribute(
        "font-stretch",
        anim=False,
        types=empty_list,
        const=frozenset(
            [
                "condensed",
                "normal",
                "ultra-condensed",
                "expanded",
                "narrower",
                "inherit",
                "semi-condensed",
                "extra-condensed",
                "ultra-expanded",
                "wider",
                "semi-expanded",
                "extra-expanded",
            ]
        ),
    ),
    "font-style": SVGAttribute(
        "font-style",
        anim=False,
        types=empty_list,
        const=frozenset(["oblique", "inherit", "italic", "normal"]),
    ),
    "font-variant": SVGAttribute(
        "font-variant",
        anim=False,
        types=empty_list,
        const=frozenset(["small-caps", "inherit", "normal"]),
    ),
    "font-weight": SVGAttribute(
        "font-weight",
        anim=False,
        types=empty_list,
        const=frozenset(
            [
                "200",
                "900",
                "bold",
                "bolder",
                "normal",
                "300",
                "700",
                "inherit",
                "lighter",
                "400",
                "100",
                "800",
                "500",
                "600",
            ]
        ),
    ),
    "format": SVGAttribute(
        "format", anim=False, types=frozenset(["string"]), const=empty_list
    ),
    "from": SVGAttribute(
        "from", anim=False, types=frozenset(["string"]), const=empty_list
    ),
    "fx": SVGAttribute(
        "fx", anim=True, types=frozenset(["coordinate"]), const=empty_list
    ),
    "fy": SVGAttribute(
        "fy", anim=True, types=frozenset(["coordinate"]), const=empty_list
    ),
    "g1": SVGAttribute(
        "g1", anim=False, types=frozenset(["list-of-name"]), const=empty_list
    ),
    "g2": SVGAttribute(
        "g2", anim=False, types=frozenset(["list-of-name"]), const=empty_list
    ),
    "glyph-name": SVGAttribute(
        "glyph-name", anim=False, types=frozenset(["list-of-name"]), const=empty_list
    ),
    "glyph-orientation-horizontal": SVGAttribute(
        "glyph-orientation-horizontal",
        anim=True,
        types=frozenset(["angle"]),
        const=frozenset(["inherit"]),
    ),
    "glyph-orientation-vertical": SVGAttribute(
        "glyph-orientation-vertical",
        anim=True,
        types=frozenset(["angle"]),
        const=frozenset(["auto", "inherit"]),
    ),
    "glyphRef": SVGAttribute(
        "glyphRef", anim=False, types=frozenset(["string"]), const=empty_list
    ),
    "gradientTransform": SVGAttribute(
        "gradientTransform",
        anim=True,
        types=frozenset(["transform-list"]),
        const=empty_list,
    ),
    "gradientUnits": SVGAttribute(
        "gradientUnits",
        anim=True,
        types=empty_list,
        const=frozenset(["userSpaceOnUse", "objectBoundingBox"]),
    ),
    "hanging": SVGAttribute(
        "hanging", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "height": SVGAttribute(
        "height", anim=True, types=frozenset(["length"]), const=empty_list
    ),
    "horiz-adv-x": SVGAttribute(
        "horiz-adv-x", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "horiz-origin-x": SVGAttribute(
        "horiz-origin-x", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "horiz-origin-y": SVGAttribute(
        "horiz-origin-y", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "id": SVGAttribute("id", anim=False, types=frozenset(["name"]), const=empty_list),
    "ideographic": SVGAttribute(
        "ideographic", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "image-rendering": SVGAttribute(
        "image-rendering",
        anim=True,
        types=empty_list,
        const=frozenset(["auto", "optimizeQuality", "optimizeSpeed", "inherit"]),
    ),
    "in": SVGAttribute(
        "in",
        anim=True,
        types=frozenset(["name"]),
        const=frozenset(
            [
                "SourceAlpha",
                "SourceGraphic",
                "BackgroundAlpha",
                "BackgroundImage",
                "StrokePaint",
                "FillPaint",
            ]
        ),
    ),
    "in2": SVGAttribute(
        "in2",
        anim=True,
        types=frozenset(["name"]),
        const=frozenset(
            [
                "SourceAlpha",
                "SourceGraphic",
                "BackgroundAlpha",
                "BackgroundImage",
                "StrokePaint",
                "FillPaint",
            ]
        ),
    ),
    "intercept": SVGAttribute(
        "intercept", anim=True, types=frozenset(["number"]), const=empty_list
    ),
    "k": SVGAttribute("k", anim=False, types=frozenset(["number"]), const=empty_list),
    "k1": SVGAttribute("k1", anim=True, types=frozenset(["number"]), const=empty_list),
    "k2": SVGAttribute("k2", anim=True, types=frozenset(["number"]), const=empty_list),
    "k3": SVGAttribute("k3", anim=True, types=frozenset(["number"]), const=empty_list),
    "k4": SVGAttribute("k4", anim=True, types=frozenset(["number"]), const=empty_list),
    "kernelMatrix": SVGAttribute(
        "kernelMatrix", anim=True, types=frozenset(["list-of-number"]), const=empty_list
    ),
    "kernelUnitLength": SVGAttribute(
        "kernelUnitLength",
        anim=True,
        types=frozenset(["number-optional-number"]),
        const=empty_list,
    ),
    "kerning": SVGAttribute(
        "kerning",
        anim=True,
        types=frozenset(["length"]),
        const=frozenset(["auto", "inherit"]),
    ),
    "keyPoints": SVGAttribute(
        "keyPoints", anim=False, types=frozenset(["semicolon-list"]), const=empty_list
    ),
    "keySplines": SVGAttribute(
        "keySplines", anim=False, types=frozenset(["semicolon-list"]), const=empty_list
    ),
    "keyTimes": SVGAttribute(
        "keyTimes", anim=False, types=frozenset(["semicolon-list"]), const=empty_list
    ),
    "lang": SVGAttribute(
        "lang", anim=False, types=frozenset(["name"]), const=empty_list
    ),
    "lengthAdjust": SVGAttribute(
        "lengthAdjust",
        anim=True,
        types=empty_list,
        const=frozenset(["spacingAndGlyphs", "spacing"]),
    ),
    "letter-spacing": SVGAttribute(
        "letter-spacing",
        anim=True,
        types=frozenset(["length"]),
        const=frozenset(["inherit", "normal"]),
    ),
    "lighting-color": SVGAttribute(
        "lighting-color",
        anim=True,
        types=frozenset(["color", "icccolor"]),
        const=frozenset(["currentColor", "inherit"]),
    ),
    "limitingConeAngle": SVGAttribute(
        "limitingConeAngle", anim=True, types=frozenset(["number"]), const=empty_list
    ),
    "local": SVGAttribute(
        "local", anim=True, types=frozenset(["string"]), const=empty_list
    ),
    "marker": SVGAttribute(
        "marker",
        anim=True,
        types=frozenset(["FuncIRI"]),
        const=frozenset(["none", "inherit"]),
    ),
    "marker-end": SVGAttribute(
        "marker-end",
        anim=True,
        types=frozenset(["FuncIRI"]),
        const=frozenset(["none", "inherit"]),
    ),
    "marker-mid": SVGAttribute(
        "marker-mid",
        anim=True,
        types=frozenset(["FuncIRI"]),
        const=frozenset(["none", "inherit"]),
    ),
    "marker-start": SVGAttribute(
        "marker-start",
        anim=True,
        types=frozenset(["FuncIRI"]),
        const=frozenset(["none", "inherit"]),
    ),
    "markerHeight": SVGAttribute(
        "markerHeight", anim=True, types=frozenset(["length"]), const=empty_list
    ),
    "markerUnits": SVGAttribute(
        "markerUnits",
        anim=True,
        types=empty_list,
        const=frozenset(["userSpaceOnUse", "strokeWidth"]),
    ),
    "markerWidth": SVGAttribute(
        "markerWidth", anim=True, types=frozenset(["length"]), const=empty_list
    ),
    "mask": SVGAttribute(
        "mask",
        anim=True,
        types=frozenset(["FuncIRI"]),
        const=frozenset(["none", "inherit"]),
    ),
    "maskContentUnits": SVGAttribute(
        "maskContentUnits",
        anim=True,
        types=empty_list,
        const=frozenset(["userSpaceOnUse", "objectBoundingBox"]),
    ),
    "maskUnits": SVGAttribute(
        "maskUnits",
        anim=True,
        types=empty_list,
        const=frozenset(["userSpaceOnUse", "objectBoundingBox"]),
    ),
    "mathematical": SVGAttribute(
        "mathematical", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "max": SVGAttribute(
        "max", anim=False, types=frozenset(["time"]), const=frozenset(["media"])
    ),
    "media": SVGAttribute(
        "media",
        anim=False,
        types=empty_list,
        const=frozenset(
            [
                "all",
                "aureal",
                "braille",
                "embossed",
                "handheld",
                "print",
                "projection",
                "screen",
                "tty",
                "tv",
            ]
        ),
    ),
    "method": SVGAttribute(
        "method", anim=True, types=empty_list, const=frozenset(["stretch", "align"])
    ),
    "min": SVGAttribute(
        "min", anim=False, types=frozenset(["time"]), const=frozenset(["media"])
    ),
    "mode": SVGAttribute(
        "mode",
        anim=True,
        types=empty_list,
        const=frozenset(["multiply", "screen", "darken", "lighten", "normal"]),
    ),
    "name": SVGMultiAttribute(
        {
            "* font-face-name": SVGAttribute(
                "name", anim=False, types=frozenset(["anything"]), const=empty_list
            ),
            "color-profile": SVGAttribute(
                "name", anim=False, types=frozenset(["name"]), const=empty_list
            ),
        }
    ),
    "numOctaves": SVGAttribute(
        "numOctaves", anim=True, types=frozenset(["integer"]), const=empty_list
    ),
    "offset": SVGMultiAttribute(
        {
            "*": SVGAttribute(
                "offset", anim=True, types=frozenset(["number"]), const=empty_list
            ),
            "stop": SVGAttribute(
                "offset",
                anim=True,
                types=frozenset(["number", "percentage"]),
                const=empty_list,
            ),
        }
    ),
    "onabort": SVGAttribute(
        "onabort", anim=False, types=frozenset(["anything"]), const=empty_list
    ),
    "onactivate": SVGAttribute(
        "onactivate", anim=False, types=frozenset(["anything"]), const=empty_list
    ),
    "onbegin": SVGAttribute(
        "onbegin", anim=False, types=frozenset(["anything"]), const=empty_list
    ),
    "onclick": SVGAttribute(
        "onclick", anim=False, types=frozenset(["anything"]), const=empty_list
    ),
    "onend": SVGAttribute(
        "onend", anim=True, types=frozenset(["anything"]), const=empty_list
    ),
    "onerror": SVGAttribute(
        "onerror", anim=False, types=frozenset(["anything"]), const=empty_list
    ),
    "onfocusin": SVGAttribute(
        "onfocusin", anim=False, types=frozenset(["anything"]), const=empty_list
    ),
    "onfocusout": SVGAttribute(
        "onfocusout", anim=False, types=frozenset(["anything"]), const=empty_list
    ),
    "onload": SVGAttribute(
        "onload", anim=False, types=frozenset(["anything"]), const=empty_list
    ),
    "onmousedown": SVGAttribute(
        "onmousedown", anim=False, types=frozenset(["anything"]), const=empty_list
    ),
    "onmousemove": SVGAttribute(
        "onmousemove", anim=False, types=frozenset(["anything"]), const=empty_list
    ),
    "onmouseout": SVGAttribute(
        "onmouseout", anim=False, types=frozenset(["anything"]), const=empty_list
    ),
    "onmouseover": SVGAttribute(
        "onmouseover", anim=False, types=frozenset(["anything"]), const=empty_list
    ),
    "onmouseup": SVGAttribute(
        "onmouseup", anim=False, types=frozenset(["anything"]), const=empty_list
    ),
    "onrepeat": SVGAttribute(
        "onrepeat", anim=False, types=frozenset(["anything"]), const=empty_list
    ),
    "onresize": SVGAttribute(
        "onresize", anim=False, types=frozenset(["anything"]), const=empty_list
    ),
    "onscroll": SVGAttribute(
        "onscroll", anim=False, types=frozenset(["anything"]), const=empty_list
    ),
    "onunload": SVGAttribute(
        "onunload", anim=False, types=frozenset(["anything"]), const=empty_list
    ),
    "onzoom": SVGAttribute(
        "onzoom", anim=False, types=frozenset(["anything"]), const=empty_list
    ),
    "opacity": SVGAttribute(
        "opacity", anim=True, types=frozenset(["number"]), const=frozenset(["inherit"])
    ),
    "operator": SVGMultiAttribute(
        {
            "* feComposite": SVGAttribute(
                "operator",
                anim=True,
                types=empty_list,
                const=frozenset(["xor", "in", "over", "atop", "arithmetic", "out"]),
            ),
            "feMorphology": SVGAttribute(
                "operator",
                anim=True,
                types=empty_list,
                const=frozenset(["erode", "dilate"]),
            ),
        }
    ),
    "order": SVGAttribute(
        "order",
        anim=True,
        types=frozenset(["number-optional-number"]),
        const=empty_list,
    ),
    "orient": SVGAttribute(
        "orient", anim=True, types=frozenset(["angle"]), const=frozenset(["auto"])
    ),
    "orientation": SVGAttribute(
        "orientation", anim=False, types=empty_list, const=frozenset(["h", "v"])
    ),
    "origin": SVGAttribute(
        "origin", anim=False, types=empty_list, const=frozenset(["default"])
    ),
    "overflow": SVGAttribute(
        "overflow",
        anim=True,
        types=empty_list,
        const=frozenset(["visible", "hidden", "scroll", "inherit", "auto"]),
    ),
    "overline-position": SVGAttribute(
        "overline-position", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "overline-thickness": SVGAttribute(
        "overline-thickness", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "panose-1": SVGAttribute(
        "panose-1", anim=False, types=frozenset(["list-of-integer"]), const=empty_list
    ),
    "path": SVGAttribute(
        "path", anim=False, types=frozenset(["path-data"]), const=empty_list
    ),
    "pathLength": SVGAttribute(
        "pathLength", anim=True, types=frozenset(["number"]), const=empty_list
    ),
    "patternContentUnits": SVGAttribute(
        "patternContentUnits",
        anim=True,
        types=empty_list,
        const=frozenset(["userSpaceOnUse", "objectBoundingBox"]),
    ),
    "patternTransform": SVGAttribute(
        "patternTransform",
        anim=True,
        types=frozenset(["transform-list"]),
        const=empty_list,
    ),
    "patternUnits": SVGAttribute(
        "patternUnits",
        anim=True,
        types=empty_list,
        const=frozenset(["userSpaceOnUse", "objectBoundingBox"]),
    ),
    "pointer-events": SVGAttribute(
        "pointer-events",
        anim=True,
        types=empty_list,
        const=frozenset(
            [
                "all",
                "visibleStroke",
                "painted",
                "none",
                "visibleFill",
                "visible",
                "stroke",
                "inherit",
                "visiblePainted",
                "fill",
            ]
        ),
    ),
    "points": SVGAttribute(
        "points", anim=True, types=frozenset(["list-of-points"]), const=empty_list
    ),
    "pointsAtX": SVGAttribute(
        "pointsAtX", anim=True, types=frozenset(["number"]), const=empty_list
    ),
    "pointsAtY": SVGAttribute(
        "pointsAtY", anim=True, types=frozenset(["number"]), const=empty_list
    ),
    "pointsAtZ": SVGAttribute(
        "pointsAtZ", anim=True, types=frozenset(["number"]), const=empty_list
    ),
    "preserveAlpha": SVGAttribute(
        "preserveAlpha", anim=True, types=empty_list, const=frozenset(["true", "false"])
    ),
    "preserveAspectRatio": SVGAttribute(
        "preserveAspectRatio", anim=True, types=frozenset("string"), const=empty_list
    ),
    "primitiveUnits": SVGAttribute(
        "primitiveUnits",
        anim=True,
        types=empty_list,
        const=frozenset(["userSpaceOnUse", "objectBoundingBox"]),
    ),
    "r": SVGAttribute("r", anim=True, types=frozenset(["length"]), const=empty_list),
    "radius": SVGAttribute(
        "radius",
        anim=True,
        types=frozenset(["number-optional-number"]),
        const=empty_list,
    ),
    "refX": SVGAttribute(
        "refX", anim=True, types=frozenset(["coordinate"]), const=empty_list
    ),
    "refY": SVGAttribute(
        "refY", anim=True, types=frozenset(["coordinate"]), const=empty_list
    ),
    "rendering-intent": SVGAttribute(
        "rendering-intent",
        anim=False,
        types=empty_list,
        const=frozenset(
            [
                "auto",
                "saturation",
                "perceptual",
                "relative-colorimetric",
                "absolute-colorimetric",
            ]
        ),
    ),
    "repeatCount": SVGAttribute(
        "repeatCount",
        anim=False,
        types=frozenset(["number"]),
        const=frozenset(["indefinite"]),
    ),
    "repeatDur": SVGAttribute(
        "repeatDur",
        anim=False,
        types=frozenset(["time"]),
        const=frozenset(["indefinite"]),
    ),
    "requiredExtensions": SVGAttribute(
        "requiredExtensions", anim=False, types=frozenset(["string"]), const=empty_list
    ),
    "requiredFeatures": SVGAttribute(
        "requiredFeatures", anim=False, types=frozenset(["string"]), const=empty_list
    ),
    "restart": SVGAttribute(
        "restart",
        anim=False,
        types=empty_list,
        const=frozenset(["always", "never", "whenNotActive"]),
    ),
    "result": SVGAttribute(
        "result", anim=True, types=frozenset(["list-of-name"]), const=empty_list
    ),
    "rotate": SVGMultiAttribute(
        {
            "* altGlyph text tref tspan": SVGAttribute(
                "rotate",
                anim=True,
                types=frozenset(["list-of-number"]),
                const=empty_list,
            ),
            "animateMotion": SVGAttribute(
                "rotate",
                anim=False,
                types=frozenset(["number"]),
                const=frozenset(["auto", "auto-reverse"]),
            ),
        }
    ),
    "rx": SVGAttribute("rx", anim=True, types=frozenset(["length"]), const=empty_list),
    "ry": SVGAttribute("ry", anim=True, types=frozenset(["length"]), const=empty_list),
    "scale": SVGAttribute(
        "scale", anim=True, types=frozenset(["number"]), const=empty_list
    ),
    "seed": SVGAttribute(
        "seed", anim=True, types=frozenset(["number"]), const=empty_list
    ),
    "shape-rendering": SVGAttribute(
        "shape-rendering",
        anim=True,
        types=empty_list,
        const=frozenset(
            ["auto", "optimizeSpeed", "inherit", "geometricPrecision", "crispEdges"]
        ),
    ),
    "slope": SVGMultiAttribute(
        {
            "*": SVGAttribute(
                "slope", anim=True, types=frozenset(["number"]), const=empty_list
            ),
            "font-face": SVGAttribute(
                "slope", anim=False, types=frozenset(["number"]), const=empty_list
            ),
        }
    ),
    "spacing": SVGAttribute(
        "spacing", anim=True, types=empty_list, const=frozenset(["auto", "exact"])
    ),
    "specularConstant": SVGAttribute(
        "specularConstant", anim=True, types=frozenset(["number"]), const=empty_list
    ),
    "specularExponent": SVGAttribute(
        "specularExponent", anim=True, types=frozenset(["number"]), const=empty_list
    ),
    "spreadMethod": SVGAttribute(
        "spreadMethod",
        anim=True,
        types=empty_list,
        const=frozenset(["reflect", "repeat", "pad"]),
    ),
    "startOffset": SVGAttribute(
        "startOffset", anim=True, types=frozenset(["length"]), const=empty_list
    ),
    "stdDeviation": SVGAttribute(
        "stdDeviation",
        anim=True,
        types=frozenset(["number-optional-number"]),
        const=empty_list,
    ),
    "stemh": SVGAttribute(
        "stemh", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "stemv": SVGAttribute(
        "stemv", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "stitchTiles": SVGAttribute(
        "stitchTiles",
        anim=True,
        types=empty_list,
        const=frozenset(["noStitch", "stitch"]),
    ),
    "stop-color": SVGAttribute(
        "stop-color",
        anim=True,
        types=frozenset(["color", "icccolor"]),
        const=frozenset(["currentColor", "inherit"]),
    ),
    "stop-opacity": SVGAttribute(
        "stop-opacity",
        anim=True,
        types=frozenset(["number"]),
        const=frozenset(["inherit"]),
    ),
    "strikethrough-position": SVGAttribute(
        "strikethrough-position",
        anim=False,
        types=frozenset(["number"]),
        const=empty_list,
    ),
    "strikethrough-thickness": SVGAttribute(
        "strikethrough-thickness",
        anim=False,
        types=frozenset(["number"]),
        const=empty_list,
    ),
    "string": SVGAttribute(
        "string", anim=False, types=frozenset("anything"), const=empty_list
    ),
    "stroke": SVGAttribute(
        "stroke", anim=True, types=frozenset(["paint"]), const=empty_list
    ),
    "stroke-dasharray": SVGAttribute(
        "stroke-dasharray",
        anim=True,
        types=frozenset(["list-of-length"]),
        const=frozenset(["none", "inherit"]),
    ),
    "stroke-dashoffset": SVGAttribute(
        "stroke-dashoffset",
        anim=True,
        types=frozenset(["length"]),
        const=frozenset(["inherit"]),
    ),
    "stroke-linecap": SVGAttribute(
        "stroke-linecap",
        anim=True,
        types=empty_list,
        const=frozenset(["square", "round", "inherit", "butt"]),
    ),
    "stroke-linejoin": SVGAttribute(
        "stroke-linejoin",
        anim=True,
        types=empty_list,
        const=frozenset(["bevel", "miter", "round", "inherit"]),
    ),
    "stroke-miterlimit": SVGAttribute(
        "stroke-miterlimit",
        anim=True,
        types=frozenset(["number"]),
        const=frozenset(["inherit"]),
    ),
    "stroke-opacity": SVGAttribute(
        "stroke-opacity",
        anim=True,
        types=frozenset(["number"]),
        const=frozenset(["inherit"]),
    ),
    "stroke-width": SVGAttribute(
        "stroke-width",
        anim=True,
        types=frozenset(["length"]),
        const=frozenset(["inherit"]),
    ),
    "style": SVGAttribute(
        "style", anim=False, types=frozenset("anything"), const=empty_list
    ),
    "surfaceScale": SVGAttribute(
        "surfaceScale", anim=True, types=frozenset(["number"]), const=empty_list
    ),
    "systemLanguage": SVGAttribute(
        "systemLanguage", anim=False, types=frozenset(["string"]), const=empty_list
    ),
    "tableValues": SVGAttribute(
        "tableValues", anim=True, types=frozenset(["list-of-number"]), const=empty_list
    ),
    "target": SVGAttribute(
        "target",
        anim=True,
        types=frozenset(["XML-Name"]),
        const=frozenset(["_replace", "_self", "_parent", "_top", "_blank"]),
    ),
    "targetX": SVGAttribute(
        "targetX", anim=True, types=frozenset(["integer"]), const=empty_list
    ),
    "targetY": SVGAttribute(
        "targetY", anim=True, types=frozenset(["integer"]), const=empty_list
    ),
    "text-anchor": SVGAttribute(
        "text-anchor",
        anim=True,
        types=empty_list,
        const=frozenset(["start", "end", "inherit", "middle"]),
    ),
    "text-decoration": SVGAttribute(
        "text-decoration",
        anim=True,
        types=frozenset(["list-of-text-decoration-style"]),
        const=frozenset(["", "none", "inherit"]),
    ),
    "text-rendering": SVGAttribute(
        "text-rendering",
        anim=True,
        types=empty_list,
        const=frozenset(
            [
                "auto",
                "optimizeSpeed",
                "optimizeLegibility",
                "geometricPrecision",
                "inherit",
            ]
        ),
    ),
    "textLength": SVGAttribute(
        "textLength", anim=True, types=frozenset(["length"]), const=empty_list
    ),
    "title": SVGAttribute(
        "title", anim=False, types=frozenset(["string"]), const=empty_list
    ),
    "to": SVGAttribute("to", anim=False, types=frozenset(["string"]), const=empty_list),
    "transform": SVGAttribute(
        "transform", anim=True, types=frozenset(["transform-list"]), const=empty_list
    ),
    "type": SVGMultiAttribute(
        {
            "* feColorMatrix": SVGAttribute(
                "type",
                anim=True,
                types=empty_list,
                const=frozenset(
                    ["matrix", "saturate", "hueRotate", "luminanceToAlpha"]
                ),
            ),
            "feTurbulence": SVGAttribute(
                "type",
                anim=True,
                types=empty_list,
                const=frozenset(["fractalNoise", "turbulence"]),
            ),
            "feFuncR feFuncG feFuncB feFuncA": SVGAttribute(
                "type",
                anim=True,
                types=empty_list,
                const=frozenset(["identity", "table", "discrete", "linear", "gamma"]),
            ),
            "script style": SVGAttribute(
                "type", anim=False, types=frozenset(["content-type"]), const=empty_list
            ),
            "animateTransform": SVGAttribute(
                "type",
                anim=False,
                types=empty_list,
                const=frozenset(["translate", "scale", "rotate", "skewX", "skewY"]),
            ),
        }
    ),
    "u1": SVGAttribute("u1", anim=False, types=frozenset(["string"]), const=empty_list),
    "u2": SVGAttribute("u2", anim=False, types=frozenset(["string"]), const=empty_list),
    "underline-position": SVGAttribute(
        "underline-position", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "underline-thickness": SVGAttribute(
        "underline-thickness", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "unicode": SVGAttribute(
        "unicode", anim=False, types=frozenset(["string"]), const=empty_list
    ),
    "unicode-bidi": SVGAttribute(
        "unicode-bidi",
        anim=False,
        types=empty_list,
        const=frozenset(["embed", "inherit", "bidi-override", "normal"]),
    ),
    "unicode-range": SVGAttribute(
        "unicode-range", anim=False, types=frozenset(["string"]), const=empty_list
    ),
    "units-per-em": SVGAttribute(
        "units-per-em", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "v-alphabetic": SVGAttribute(
        "v-alphabetic", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "v-hanging": SVGAttribute(
        "v-hanging", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "v-ideographic": SVGAttribute(
        "v-ideographic", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "v-mathematical": SVGAttribute(
        "v-mathematical", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "values": SVGMultiAttribute(
        {
            "*": SVGAttribute(
                "values",
                anim=False,
                types=frozenset(["semicolon-list"]),
                const=empty_list,
            ),
            "feColorMatrix": SVGAttribute(
                "values",
                anim=True,
                types=frozenset(["list-of-number"]),
                const=empty_list,
            ),
        }
    ),
    "version": SVGAttribute(
        "version", anim=False, types=empty_list, const=frozenset(["1.1", "1.2"])
    ),
    "vert-adv-y": SVGAttribute(
        "vert-adv-y", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "vert-origin-x": SVGAttribute(
        "vert-origin-x", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "vert-origin-y": SVGAttribute(
        "vert-origin-y", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "viewBox": SVGAttribute(
        "viewBox", anim=True, types=frozenset(["four-numbers"]), const=empty_list
    ),
    "viewTarget": SVGAttribute(
        "viewTarget",
        anim=False,
        types=frozenset(["list-of-XML-Name"]),
        const=empty_list,
    ),
    "visibility": SVGAttribute(
        "visibility",
        anim=True,
        types=empty_list,
        const=frozenset(["visible", "hidden", "collapse", "inherit"]),
    ),
    "width": SVGAttribute(
        "width", anim=True, types=frozenset(["length"]), const=empty_list
    ),
    "widths": SVGAttribute(
        "widths", anim=False, types=frozenset(["string"]), const=empty_list
    ),
    "word-spacing": SVGAttribute(
        "word-spacing",
        anim=True,
        types=frozenset(["length"]),
        const=frozenset(["inherit", "normal"]),
    ),
    "writing-mode": SVGAttribute(
        "writing-mode",
        anim=False,
        types=empty_list,
        const=frozenset(["rl-tb", "lr", "rl", "tb-rl", "lr-tb", "inherit", "tb"]),
    ),
    "x": SVGMultiAttribute(
        {
            "*": SVGAttribute(
                "x", anim=True, types=frozenset(["coordinate"]), const=empty_list
            ),
            "altGlyph text tref tspan": SVGAttribute(
                "x",
                anim=True,
                types=frozenset(["list-of-coordinate"]),
                const=empty_list,
            ),
            "fePointLight feSpotLight glyphRef": SVGAttribute(
                "x", anim=True, types=frozenset(["number"]), const=empty_list
            ),
        }
    ),
    "x-height": SVGAttribute(
        "x-height", anim=False, types=frozenset(["number"]), const=empty_list
    ),
    "x1": SVGAttribute(
        "x1", anim=True, types=frozenset(["list-of-coordinate"]), const=empty_list
    ),
    "x2": SVGAttribute(
        "x2", anim=True, types=frozenset(["list-of-coordinate"]), const=empty_list
    ),
    "xChannelSelector": SVGAttribute(
        "xChannelSelector",
        anim=True,
        types=empty_list,
        const=frozenset(["A", "B", "R", "G"]),
    ),
    "xlink:actuate": SVGMultiAttribute(
        {
            "*": SVGAttribute(
                "xlink:actuate",
                anim=False,
                types=empty_list,
                const=frozenset(["onLoad"]),
            ),
            "a": SVGAttribute(
                "xlink:actuate",
                anim=False,
                types=empty_list,
                const=frozenset(["onRequest"]),
            ),
        }
    ),
    "xlink:arcrole": SVGAttribute(
        "xlink:arcrole", anim=False, types=frozenset(["IRI"]), const=empty_list
    ),
    "xlink:href": SVGAttribute(
        "xlink:href", anim=False, types=frozenset(["IRI"]), const=empty_list
    ),
    "xlink:role": SVGAttribute(
        "xlink:role", anim=False, types=frozenset(["IRI"]), const=empty_list
    ),
    "xlink:show": SVGMultiAttribute(
        {
            "*": SVGAttribute(
                "xlink:show",
                anim=False,
                types=empty_list,
                const=frozenset(["other", "new", "replace", "none", "embed"]),
            ),
            "a": SVGAttribute(
                "xlink:show",
                anim=False,
                types=empty_list,
                const=frozenset(["new", "replace"]),
            ),
        }
    ),
    "xlink:title": SVGAttribute(
        "xlink:title", anim=False, types=frozenset(["string"]), const=empty_list
    ),
    "xlink:type": SVGAttribute(
        "xlink:type", anim=False, types=empty_list, const=frozenset(["simple"])
    ),
    "xmlns": SVGAttribute(
        "xmlns", anim=False, types=frozenset(["IRI"]), const=empty_list
    ),
    "xmlns:xlink": SVGAttribute(
        "xmlns:xlink", anim=False, types=frozenset(["IRI"]), const=empty_list
    ),
    "xmlns:ev": SVGAttribute(
        "xmlns:ev", anim=False, types=frozenset(["IRI"]), const=empty_list
    ),
    "xml:base": SVGAttribute(
        "xml:base", anim=False, types=frozenset(["IRI"]), const=empty_list
    ),
    "xml:lang": SVGAttribute(
        "xml:lang", anim=False, types=frozenset(["name"]), const=empty_list
    ),
    "xml:space": SVGAttribute(
        "xml:space",
        anim=False,
        types=empty_list,
        const=frozenset(["default", "preserve"]),
    ),
    "y": SVGMultiAttribute(
        {
            "*": SVGAttribute(
                "y", anim=True, types=frozenset(["coordinate"]), const=empty_list
            ),
            "altGlyph text tref tspan": SVGAttribute(
                "y",
                anim=True,
                types=frozenset(["list-of-coordinate"]),
                const=empty_list,
            ),
            "fePointLight feSpotLight glyphRef": SVGAttribute(
                "y", anim=True, types=frozenset(["number"]), const=empty_list
            ),
        }
    ),
    "y1": SVGAttribute(
        "y1", anim=True, types=frozenset(["list-of-coordinate"]), const=empty_list
    ),
    "y2": SVGAttribute(
        "y2", anim=True, types=frozenset(["list-of-coordinate"]), const=empty_list
    ),
    "yChannelSelector": SVGAttribute(
        "yChannelSelector",
        anim=True,
        types=empty_list,
        const=frozenset(["A", "B", "R", "G"]),
    ),
    "z": SVGAttribute("z", anim=True, types=frozenset(["number"]), const=empty_list),
    "zoomAndPan": SVGAttribute(
        "zoomAndPan",
        anim=False,
        types=empty_list,
        const=frozenset(["disable", "magnify"]),
    ),
}

presentation_attributes = frozenset(
    [
        "alignment-baseline",
        "baseline-shift",
        "clip",
        "clip-path",
        "clip-rule",
        "color",
        "color-interpolation",
        "color-interpolation-filters",
        "color-profile",
        "color-rendering",
        "cursor",
        "direction",
        "display",
        "dominant-baseline",
        "enable-background",
        "fill",
        "fill-opacity",
        "fill-rule",
        "filter",
        "flood-color",
        "flood-opacity",
        "font-family",
        "font-size",
        "font-size-adjust",
        "font-stretch",
        "font-style",
        "font-variant",
        "font-weight",
        "glyph-orientation-horizontal",
        "glyph-orientation-vertical",
        "image-rendering",
        "kerning",
        "letter-spacing",
        "lighting-color",
        "marker",
        "marker-end",
        "marker-mid",
        "marker-start",
        "mask",
        "opacity",
        "overflow",
        "pointer-events",
        "shape-rendering",
        "stop-color",
        "stop-opacity",
        "stroke",
        "stroke-dasharray",
        "stroke-dashoffset",
        "stroke-linecap",
        "stroke-linejoin",
        "stroke-miterlimit",
        "stroke-opacity",
        "stroke-width",
        "text-anchor",
        "text-decoration",
        "text-rendering",
        "unicode-bidi",
        "visibility",
        "word-spacing",
        "writing-mode",
    ]
)

elements = {
    "a": SVGElement(
        "a",
        attributes=frozenset(
            [
                "xlink:title",
                "xml:base",
                "onmouseup",
                "onmouseout",
                "requiredExtensions",
                "onfocusout",
                "xml:space",
                "xlink:href",
                "systemLanguage",
                "onmouseover",
                "xlink:type",
                "externalResourcesRequired",
                "id",
                "xlink:actuate",
                "onload",
                "style",
                "xlink:show",
                "target",
                "onactivate",
                "onmousedown",
                "transform",
                "class",
                "xlink:role",
                "requiredFeatures",
                "xml:lang",
                "onmousemove",
                "xmlns:xlink",
                "onclick",
                "xlink:arcrole",
                "onfocusin",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "set",
                "text",
                "image",
                "font-face",
                "polyline",
                "marker",
                "animate",
                "font",
                "color-profile",
                "ellipse",
                "cursor",
                "style",
                "polygon",
                "title",
                "pattern",
                "circle",
                "radialGradient",
                "metadata",
                "defs",
                "symbol",
                "use",
                "animateMotion",
                "animateColor",
                "path",
                "line",
                "rect",
                "desc",
                "a",
                "g",
                "svg",
                "script",
                "mask",
                "altGlyphDef",
                "filter",
                "switch",
                "animateTransform",
                "linearGradient",
                "clipPath",
                "foreignObject",
                "view",
            ]
        ),
    ),
    "altGlyph": SVGElement(
        "altGlyph",
        attributes=frozenset(
            [
                "requiredExtensions",
                "onfocusout",
                "xml:space",
                "xlink:href",
                "id",
                "onload",
                "style",
                "onmousedown",
                "onmousemove",
                "onclick",
                "xlink:arcrole",
                "onfocusin",
                "xml:base",
                "onmouseup",
                "onmouseout",
                "format",
                "xlink:title",
                "systemLanguage",
                "onmouseover",
                "dx",
                "dy",
                "xlink:type",
                "externalResourcesRequired",
                "class",
                "xlink:actuate",
                "xlink:show",
                "onactivate",
                "glyphRef",
                "xlink:role",
                "requiredFeatures",
                "xml:lang",
                "y",
                "x",
                "rotate",
            ]
        ),
        properties=presentation_attributes,
        children=empty_list,
    ),
    "altGlyphDef": SVGElement(
        "altGlyphDef",
        attributes=frozenset(["xml:space", "xml:lang", "xml:base", "id"]),
        properties=empty_list,
        children=frozenset(["*"]),
    ),
    "altGlyphItem": SVGElement(
        "altGlyphItem",
        attributes=frozenset(["xml:space", "xml:lang", "xml:base", "id"]),
        properties=empty_list,
        children=frozenset(["*"]),
    ),
    "animate": SVGElement(
        "animate",
        attributes=frozenset(
            [
                "requiredExtensions",
                "from",
                "repeatCount",
                "xml:space",
                "xlink:href",
                "xlink:type",
                "attributeType",
                "repeatDur",
                "id",
                "fill",
                "onload",
                "additive",
                "calcMode",
                "min",
                "keySplines",
                "to",
                "dur",
                "xlink:arcrole",
                "onend",
                "begin",
                "xml:base",
                "max",
                "xlink:title",
                "attributeName",
                "onbegin",
                "systemLanguage",
                "accumulate",
                "end",
                "externalResourcesRequired",
                "by",
                "restart",
                "xlink:actuate",
                "xlink:show",
                "xlink:role",
                "requiredFeatures",
                "xml:lang",
                "values",
                "keyTimes",
                "onrepeat",
            ]
        ),
        properties=empty_list,
        children=frozenset(["desc", "metadata", "title"]),
    ),
    "animateColor": SVGElement(
        "animateColor",
        attributes=frozenset(
            [
                "requiredExtensions",
                "from",
                "repeatCount",
                "xml:space",
                "xlink:href",
                "xlink:type",
                "attributeType",
                "repeatDur",
                "id",
                "fill",
                "onload",
                "additive",
                "calcMode",
                "min",
                "keySplines",
                "to",
                "dur",
                "xlink:arcrole",
                "onend",
                "begin",
                "xml:base",
                "max",
                "xlink:title",
                "attributeName",
                "onbegin",
                "systemLanguage",
                "accumulate",
                "end",
                "externalResourcesRequired",
                "by",
                "restart",
                "xlink:actuate",
                "xlink:show",
                "xlink:role",
                "requiredFeatures",
                "xml:lang",
                "values",
                "keyTimes",
                "onrepeat",
            ]
        ),
        properties=empty_list,
        children=frozenset(["desc", "metadata", "title"]),
    ),
    "animateMotion": SVGElement(
        "animateMotion",
        attributes=frozenset(
            [
                "origin",
                "requiredExtensions",
                "from",
                "repeatCount",
                "xml:space",
                "xlink:href",
                "xlink:type",
                "repeatDur",
                "id",
                "fill",
                "onload",
                "additive",
                "calcMode",
                "min",
                "keySplines",
                "to",
                "dur",
                "xlink:arcrole",
                "onend",
                "begin",
                "xlink:title",
                "xml:base",
                "max",
                "end",
                "keyPoints",
                "onbegin",
                "systemLanguage",
                "accumulate",
                "path",
                "externalResourcesRequired",
                "by",
                "restart",
                "xlink:actuate",
                "xlink:show",
                "xlink:role",
                "requiredFeatures",
                "xml:lang",
                "values",
                "keyTimes",
                "onrepeat",
                "rotate",
            ]
        ),
        properties=empty_list,
        children=frozenset(["desc", "metadata", "mpath", "title"]),
    ),
    "animateTransform": SVGElement(
        "animateTransform",
        attributes=frozenset(
            [
                "requiredExtensions",
                "from",
                "repeatCount",
                "xml:space",
                "xlink:href",
                "xlink:type",
                "attributeType",
                "repeatDur",
                "id",
                "fill",
                "onload",
                "additive",
                "calcMode",
                "min",
                "keySplines",
                "to",
                "dur",
                "xlink:arcrole",
                "type",
                "onend",
                "begin",
                "xml:base",
                "max",
                "xlink:title",
                "attributeName",
                "onbegin",
                "systemLanguage",
                "accumulate",
                "end",
                "externalResourcesRequired",
                "by",
                "restart",
                "xlink:actuate",
                "xlink:show",
                "xlink:role",
                "requiredFeatures",
                "xml:lang",
                "values",
                "keyTimes",
                "onrepeat",
            ]
        ),
        properties=empty_list,
        children=frozenset(["desc", "metadata", "title"]),
    ),
    "circle": SVGElement(
        "circle",
        attributes=frozenset(
            [
                "xml:base",
                "onmouseup",
                "onmouseout",
                "requiredExtensions",
                "onfocusout",
                "xml:space",
                "cy",
                "cx",
                "onmouseover",
                "externalResourcesRequired",
                "id",
                "onload",
                "style",
                "onactivate",
                "onmousedown",
                "transform",
                "class",
                "requiredFeatures",
                "r",
                "onmousemove",
                "onclick",
                "xml:lang",
                "onfocusin",
                "systemLanguage",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "animateMotion",
                "set",
                "title",
                "animateColor",
                "animateTransform",
                "animate",
                "metadata",
                "desc",
            ]
        ),
    ),
    "clipPath": SVGElement(
        "clipPath",
        attributes=frozenset(
            [
                "clipPathUnits",
                "style",
                "xml:base",
                "requiredExtensions",
                "xml:space",
                "transform",
                "id",
                "requiredFeatures",
                "xml:lang",
                "externalResourcesRequired",
                "class",
                "systemLanguage",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "set",
                "animate",
                "text",
                "use",
                "animateColor",
                "polyline",
                "path",
                "line",
                "ellipse",
                "rect",
                "desc",
                "animateMotion",
                "polygon",
                "title",
                "animateTransform",
                "circle",
                "metadata",
            ]
        ),
    ),
    "color-profile": SVGElement(
        "color-profile",
        attributes=frozenset(
            [
                "xlink:actuate",
                "xlink:show",
                "xml:base",
                "name",
                "rendering-intent",
                "xml:space",
                "xlink:href",
                "xlink:role",
                "xml:lang",
                "xlink:type",
                "xlink:title",
                "xlink:arcrole",
                "local",
                "id",
            ]
        ),
        properties=empty_list,
        children=frozenset(["desc", "metadata", "title"]),
    ),
    "cursor": SVGElement(
        "cursor",
        attributes=frozenset(
            [
                "xlink:title",
                "xml:base",
                "requiredExtensions",
                "xml:space",
                "xlink:href",
                "systemLanguage",
                "xlink:type",
                "externalResourcesRequired",
                "id",
                "xlink:actuate",
                "xlink:show",
                "xlink:role",
                "requiredFeatures",
                "xml:lang",
                "y",
                "x",
                "xlink:arcrole",
            ]
        ),
        properties=empty_list,
        children=frozenset(["desc", "metadata", "title"]),
    ),
    "defs": SVGElement(
        "defs",
        attributes=frozenset(
            [
                "xml:base",
                "onmouseup",
                "onmouseout",
                "requiredExtensions",
                "onfocusout",
                "xml:space",
                "systemLanguage",
                "onmouseover",
                "externalResourcesRequired",
                "class",
                "onload",
                "style",
                "onactivate",
                "onmousedown",
                "transform",
                "id",
                "requiredFeatures",
                "xml:lang",
                "onmousemove",
                "onclick",
                "onfocusin",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "set",
                "text",
                "image",
                "font-face",
                "polyline",
                "marker",
                "animate",
                "font",
                "color-profile",
                "ellipse",
                "cursor",
                "style",
                "polygon",
                "title",
                "pattern",
                "circle",
                "radialGradient",
                "metadata",
                "defs",
                "symbol",
                "use",
                "animateMotion",
                "animateColor",
                "path",
                "line",
                "rect",
                "desc",
                "a",
                "g",
                "svg",
                "script",
                "mask",
                "altGlyphDef",
                "filter",
                "switch",
                "animateTransform",
                "linearGradient",
                "clipPath",
                "foreignObject",
                "view",
            ]
        ),
    ),
    "desc": SVGElement(
        "desc",
        attributes=frozenset(
            ["style", "xml:lang", "xml:base", "xml:space", "class", "id"]
        ),
        properties=empty_list,
        children=frozenset(["*"]),
    ),
    "ellipse": SVGElement(
        "ellipse",
        attributes=frozenset(
            [
                "xml:base",
                "onmouseup",
                "onmouseout",
                "requiredExtensions",
                "onfocusout",
                "xml:space",
                "ry",
                "cy",
                "cx",
                "onmouseover",
                "externalResourcesRequired",
                "id",
                "onload",
                "style",
                "onactivate",
                "onmousedown",
                "rx",
                "transform",
                "class",
                "requiredFeatures",
                "systemLanguage",
                "onmousemove",
                "onclick",
                "xml:lang",
                "onfocusin",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "animateMotion",
                "set",
                "title",
                "animateColor",
                "animateTransform",
                "animate",
                "desc",
                "metadata",
            ]
        ),
    ),
    "feBlend": SVGElement(
        "feBlend",
        attributes=frozenset(
            [
                "style",
                "xml:base",
                "xml:space",
                "in2",
                "height",
                "width",
                "xml:lang",
                "id",
                "result",
                "in",
                "y",
                "x",
                "class",
                "mode",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(["animate", "set"]),
    ),
    "feColorMatrix": SVGElement(
        "feColorMatrix",
        attributes=frozenset(
            [
                "style",
                "xml:base",
                "xml:space",
                "id",
                "height",
                "width",
                "xml:lang",
                "values",
                "result",
                "in",
                "y",
                "x",
                "type",
                "class",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(["animate", "set"]),
    ),
    "feComponentTransfer": SVGElement(
        "feComponentTransfer",
        attributes=frozenset(
            [
                "style",
                "xml:base",
                "xml:space",
                "height",
                "width",
                "xml:lang",
                "id",
                "result",
                "in",
                "y",
                "x",
                "class",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(["feFuncA", "feFuncR", "feFuncB", "feFuncG"]),
    ),
    "feComposite": SVGElement(
        "feComposite",
        attributes=frozenset(
            [
                "xml:base",
                "xml:space",
                "in2",
                "height",
                "result",
                "in",
                "operator",
                "class",
                "style",
                "width",
                "id",
                "k3",
                "k2",
                "k1",
                "xml:lang",
                "k4",
                "y",
                "x",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(["animate", "set"]),
    ),
    "feConvolveMatrix": SVGElement(
        "feConvolveMatrix",
        attributes=frozenset(
            [
                "xml:base",
                "xml:space",
                "kernelUnitLength",
                "edgeMode",
                "height",
                "bias",
                "result",
                "in",
                "preserveAlpha",
                "id",
                "style",
                "divisor",
                "kernelMatrix",
                "width",
                "xml:lang",
                "targetX",
                "targetY",
                "y",
                "x",
                "class2",
                "order",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(["animate", "set"]),
    ),
    "feDiffuseLighting": SVGElement(
        "feDiffuseLighting",
        attributes=frozenset(
            [
                "style",
                "xml:base",
                "xml:space",
                "diffuseConstant",
                "height",
                "kernelUnitLength",
                "width",
                "xml:lang",
                "id",
                "result",
                "in",
                "y",
                "x",
                "class",
                "surfaceScale",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "fePointLight",
                "feSpotLight",
                "title",
                "metadata",
                "feDistantLight",
                "desc",
            ]
        ),
    ),
    "feDisplacementMap": SVGElement(
        "feDisplacementMap",
        attributes=frozenset(
            [
                "xml:base",
                "xml:space",
                "yChannelSelector",
                "in2",
                "height",
                "result",
                "in",
                "class",
                "style",
                "scale",
                "id",
                "width",
                "xml:lang",
                "xChannelSelector",
                "y",
                "x",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(["animate", "set"]),
    ),
    "feDistantLight": SVGElement(
        "feDistantLight",
        attributes=frozenset(
            ["xml:lang", "elevation", "azimuth", "xml:base", "xml:space", "id"]
        ),
        properties=empty_list,
        children=frozenset(["animate", "set"]),
    ),
    "feFlood": SVGElement(
        "feFlood",
        attributes=frozenset(
            [
                "style",
                "xml:base",
                "xml:space",
                "height",
                "width",
                "xml:lang",
                "id",
                "result",
                "y",
                "x",
                "class",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(["animate", "set", "animateColor"]),
    ),
    "feFuncA": SVGElement(
        "feFuncA",
        attributes=frozenset(
            [
                "slope",
                "xml:base",
                "tableValues",
                "xml:space",
                "xml:lang",
                "intercept",
                "amplitude",
                "offset",
                "type",
                "id",
                "exponent",
            ]
        ),
        properties=empty_list,
        children=frozenset(["animate", "set"]),
    ),
    "feFuncB": SVGElement(
        "feFuncB",
        attributes=frozenset(
            [
                "slope",
                "xml:base",
                "tableValues",
                "xml:space",
                "xml:lang",
                "intercept",
                "amplitude",
                "offset",
                "type",
                "id",
                "exponent",
            ]
        ),
        properties=empty_list,
        children=frozenset(["animate", "set"]),
    ),
    "feFuncG": SVGElement(
        "feFuncG",
        attributes=frozenset(
            [
                "slope",
                "xml:base",
                "tableValues",
                "xml:space",
                "xml:lang",
                "intercept",
                "amplitude",
                "offset",
                "type",
                "id",
                "exponent",
            ]
        ),
        properties=empty_list,
        children=frozenset(["animate", "set"]),
    ),
    "feFuncR": SVGElement(
        "feFuncR",
        attributes=frozenset(
            [
                "slope",
                "xml:base",
                "tableValues",
                "xml:space",
                "xml:lang",
                "intercept",
                "amplitude",
                "offset",
                "type",
                "id",
                "exponent",
            ]
        ),
        properties=empty_list,
        children=frozenset(["animate", "set"]),
    ),
    "feGaussianBlur": SVGElement(
        "feGaussianBlur",
        attributes=frozenset(
            [
                "style",
                "xml:base",
                "xml:space",
                "height",
                "width",
                "xml:lang",
                "id",
                "result",
                "in",
                "y",
                "x",
                "stdDeviation",
                "class",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(["animate", "set"]),
    ),
    "feImage": SVGElement(
        "feImage",
        attributes=frozenset(
            [
                "xlink:title",
                "xml:base",
                "xml:space",
                "xlink:href",
                "height",
                "result",
                "xlink:type",
                "externalResourcesRequired",
                "preserveAsectRatio",
                "class",
                "xlink:actuate",
                "style",
                "xlink:show",
                "id",
                "xlink:role",
                "width",
                "xml:lang",
                "y",
                "x",
                "xlink:arcrole",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(["animate", "set", "animateColor"]),
    ),
    "feMerge": SVGElement(
        "feMerge",
        attributes=frozenset(
            [
                "style",
                "xml:base",
                "xml:space",
                "height",
                "width",
                "xml:lang",
                "id",
                "result",
                "y",
                "x",
                "class",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(["animate", "set", "feMergeNode"]),
    ),
    "feMergeNode": SVGElement(
        "feMergeNode",
        attributes=frozenset(["xml:space", "xml:lang", "xml:base", "id", "in"]),
        properties=empty_list,
        children=frozenset(["animate", "set"]),
    ),
    "feMorphology": SVGElement(
        "feMorphology",
        attributes=frozenset(
            [
                "style",
                "xml:base",
                "y",
                "xml:space",
                "id",
                "height",
                "width",
                "xml:lang",
                "radius",
                "result",
                "in",
                "operator",
                "x",
                "class",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(["animate", "set"]),
    ),
    "feOffset": SVGElement(
        "feOffset",
        attributes=frozenset(
            [
                "style",
                "xml:base",
                "xml:space",
                "in",
                "height",
                "width",
                "xml:lang",
                "id",
                "result",
                "dx",
                "dy",
                "y",
                "x",
                "class",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(["animate", "set"]),
    ),
    "fePointLight": SVGElement(
        "fePointLight",
        attributes=frozenset(
            ["xml:lang", "xml:base", "y", "x", "xml:space", "z", "id"]
        ),
        properties=empty_list,
        children=frozenset(["animate", "set"]),
    ),
    "feSpecularLighting": SVGElement(
        "feSpecularLighting",
        attributes=frozenset(
            [
                "specularConstant",
                "xml:base",
                "xml:space",
                "kernelUnitLength",
                "height",
                "result",
                "in",
                "class",
                "style",
                "id",
                "width",
                "xml:lang",
                "specularExponent",
                "y",
                "x",
                "surfaceScale",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "fePointLight",
                "feSpotLight",
                "title",
                "metadata",
                "feDistantLight",
                "desc",
            ]
        ),
    ),
    "feSpotLight": SVGElement(
        "feSpotLight",
        attributes=frozenset(
            [
                "pointsAtX",
                "xml:base",
                "xml:space",
                "limitingConeAngle",
                "xml:lang",
                "specularExponent",
                "pointsAtZ",
                "y",
                "x",
                "pointsAtY",
                "z",
                "id",
            ]
        ),
        properties=empty_list,
        children=frozenset(["animate", "set"]),
    ),
    "feTile": SVGElement(
        "feTile",
        attributes=frozenset(
            [
                "style",
                "xml:base",
                "xml:space",
                "height",
                "width",
                "xml:lang",
                "id",
                "result",
                "in",
                "y",
                "x",
                "class",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(["animate", "set"]),
    ),
    "feTurbulence": SVGElement(
        "feTurbulence",
        attributes=frozenset(
            [
                "xml:base",
                "baseFrequency",
                "xml:space",
                "stitchTiles",
                "height",
                "width",
                "xml:lang",
                "id",
                "result",
                "x",
                "y",
                "numOctaves",
                "type",
                "seed",
            ]
        ),
        properties=presentation_attributes,
        children=empty_list,
    ),
    "filter": SVGElement(
        "filter",
        attributes=frozenset(
            [
                "xlink:title",
                "xml:base",
                "xml:space",
                "xlink:href",
                "height",
                "xlink:type",
                "externalResourcesRequired",
                "class",
                "xlink:actuate",
                "style",
                "xlink:show",
                "filterRes",
                "primitiveUnits",
                "id",
                "xlink:role",
                "width",
                "xml:lang",
                "y",
                "x",
                "xlink:arcrole",
                "filterUnits",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "set",
                "animate",
                "metadata",
                "desc",
                "feBlend",
                "feColorMatrix",
                "feComponentTransfer",
                "feComposite",
                "feConvolveMatrix",
                "feDiffuseLighting",
                "feDisplacementMap",
                "feFlood",
                "feGaussianBlur",
                "feImage",
                "feMerge",
                "feMorphology",
                "feOffset",
                "feSpecularLighting",
                "feTile",
                "feTurbulence",
            ]
        ),
    ),
    "font": SVGElement(
        "font",
        attributes=frozenset(
            [
                "xml:space",
                "id",
                "xml:lang",
                "xml:base",
                "class",
                "style",
                "externalResourcesRequired",
                "horiz-origin-x",
                "horiz-origin-y",
                "horiz-adv-x",
                "vert-origin-x",
                "vert-origin-y",
                "vert-adv-y",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "title",
                "metadata",
                "missing-glyph",
                "font-face",
                "vkern",
                "hkern",
                "glyph",
                "desc",
            ]
        ),
    ),
    "font-face": SVGElement(
        "font-face",
        attributes=frozenset(
            [
                "mathematical",
                "slope",
                "font-size",
                "xml:space",
                "v-hanging",
                "hanging",
                "overline-thickness",
                "ascent",
                "id",
                "strikethrough-position",
                "underline-position",
                "descent",
                "cap-height",
                "units-per-em",
                "font-style",
                "unicode-range",
                "font-stretch",
                "font-variant",
                "x-height",
                "font-weight",
                "xml:base",
                "panose-1",
                "strikethrough-thickness",
                "stemh",
                "v-alphabetic",
                "stemv",
                "bbox",
                "underline-thickness",
                "font-family",
                "v-mathematical",
                "v-ideographic",
                "ideographic",
                "overline-position",
                "widths",
                "xml:lang",
                "accent-height",
                "alphabetic",
            ]
        ),
        properties=empty_list,
        children=frozenset(["desc", "metadata", "font-face-src", "title"]),
    ),
    "font-face-format": SVGElement(
        "font-face-format",
        attributes=frozenset(["xml:space", "xml:lang", "xml:base", "id"]),
        properties=empty_list,
        children=empty_list,
    ),
    "font-face-name": SVGElement(
        "font-face-name",
        attributes=frozenset(["xml:space", "xml:lang", "xml:base", "id", "name"]),
        properties=empty_list,
        children=empty_list,
    ),
    "font-face-uri": SVGElement(
        "font-face-uri",
        attributes=frozenset(
            [
                "xlink:actuate",
                "xlink:show",
                "xml:base",
                "xml:space",
                "xlink:href",
                "xlink:role",
                "xml:lang",
                "xlink:type",
                "xlink:title",
                "xlink:arcrole",
                "id",
            ]
        ),
        properties=empty_list,
        children=frozenset(["font-face-format"]),
    ),
    "foreignObject": SVGElement(
        "foreignObject",
        attributes=frozenset(
            [
                "xml:base",
                "onmouseup",
                "onmouseout",
                "requiredExtensions",
                "onfocusout",
                "xml:space",
                "height",
                "systemLanguage",
                "onmouseover",
                "externalResourcesRequired",
                "id",
                "onload",
                "style",
                "onactivate",
                "onmousedown",
                "transform",
                "class",
                "width",
                "requiredFeatures",
                "xml:lang",
                "onmousemove",
                "onclick",
                "y",
                "x",
                "onfocusin",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(["*"]),
    ),
    "g": SVGElement(
        "g",
        attributes=frozenset(
            [
                "xml:base",
                "onmouseup",
                "onmouseout",
                "requiredExtensions",
                "onfocusout",
                "xml:space",
                "systemLanguage",
                "onmouseover",
                "externalResourcesRequired",
                "class",
                "onload",
                "style",
                "onactivate",
                "onmousedown",
                "transform",
                "id",
                "requiredFeatures",
                "xml:lang",
                "onmousemove",
                "onclick",
                "onfocusin",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "set",
                "text",
                "image",
                "font-face",
                "polyline",
                "marker",
                "animate",
                "font",
                "color-profile",
                "ellipse",
                "cursor",
                "style",
                "polygon",
                "title",
                "pattern",
                "circle",
                "radialGradient",
                "metadata",
                "defs",
                "symbol",
                "use",
                "animateMotion",
                "animateColor",
                "path",
                "line",
                "rect",
                "desc",
                "a",
                "g",
                "svg",
                "script",
                "mask",
                "altGlyphDef",
                "filter",
                "switch",
                "animateTransform",
                "linearGradient",
                "clipPath",
                "foreignObject",
                "view",
            ]
        ),
    ),
    "glyph": SVGElement(
        "glyph",
        attributes=frozenset(
            [
                "xml:base",
                "xml:space",
                "id",
                "xml:lang",
                "class",
                "style",
                "d",
                "horiz-adv-x",
                "vert-origin-x",
                "vert-origin-y",
                "vert-adv-y",
                "unicode",
                "glyph-name",
                "orientation",
                "arabic-form",
                "lang",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "set",
                "text",
                "image",
                "font-face",
                "polyline",
                "marker",
                "animate",
                "font",
                "color-profile",
                "ellipse",
                "cursor",
                "style",
                "polygon",
                "title",
                "pattern",
                "circle",
                "radialGradient",
                "metadata",
                "defs",
                "symbol",
                "use",
                "animateMotion",
                "animateColor",
                "path",
                "line",
                "rect",
                "desc",
                "a",
                "g",
                "svg",
                "script",
                "mask",
                "altGlyphDef",
                "filter",
                "switch",
                "animateTransform",
                "linearGradient",
                "clipPath",
                "foreignObject",
                "view",
            ]
        ),
    ),
    "glyphRef": SVGElement(
        "glyphRef",
        attributes=frozenset(
            [
                "xlink:title",
                "xml:base",
                "format",
                "xml:space",
                "xlink:href",
                "dx",
                "dy",
                "xlink:type",
                "class",
                "xlink:actuate",
                "style",
                "xlink:show",
                "id",
                "xlink:role",
                "xml:lang",
                "y",
                "x",
                "xlink:arcrole",
                "glyphRef",
            ]
        ),
        properties=presentation_attributes,
        children=empty_list,
    ),
    "hkern": SVGElement(
        "hkern",
        attributes=frozenset(
            ["xml:base", "g2", "g1", "xml:space", "u1", "u2", "xml:lang", "id", "k"]
        ),
        properties=empty_list,
        children=empty_list,
    ),
    "image": SVGElement(
        "image",
        attributes=frozenset(
            [
                "requiredExtensions",
                "onfocusout",
                "xml:space",
                "xlink:href",
                "height",
                "id",
                "onload",
                "style",
                "onmousedown",
                "transform",
                "width",
                "onmousemove",
                "onclick",
                "xlink:arcrole",
                "onfocusin",
                "xml:base",
                "onmouseup",
                "onmouseout",
                "xlink:title",
                "systemLanguage",
                "onmouseover",
                "xlink:type",
                "externalResourcesRequired",
                "class",
                "xlink:actuate",
                "xlink:show",
                "onactivate",
                "xlink:role",
                "requiredFeatures",
                "xml:lang",
                "y",
                "x",
                "preserveAspectRatio",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "animateMotion",
                "set",
                "title",
                "animateColor",
                "animateTransform",
                "animate",
                "desc",
                "metadata",
            ]
        ),
    ),
    "line": SVGElement(
        "line",
        attributes=frozenset(
            [
                "xml:base",
                "onmouseup",
                "onmouseout",
                "requiredExtensions",
                "onfocusout",
                "xml:space",
                "x2",
                "systemLanguage",
                "onmouseover",
                "y1",
                "externalResourcesRequired",
                "y2",
                "id",
                "onload",
                "style",
                "x1",
                "onactivate",
                "onmousedown",
                "transform",
                "class",
                "requiredFeatures",
                "xml:lang",
                "onmousemove",
                "onclick",
                "onfocusin",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "animateMotion",
                "set",
                "title",
                "animateColor",
                "animateTransform",
                "animate",
                "desc",
                "metadata",
            ]
        ),
    ),
    "linearGradient": SVGElement(
        "linearGradient",
        attributes=frozenset(
            [
                "xlink:title",
                "xml:base",
                "xml:space",
                "xlink:href",
                "x2",
                "y1",
                "externalResourcesRequired",
                "y2",
                "class",
                "xlink:actuate",
                "xlink:role",
                "style",
                "xlink:show",
                "spreadMethod",
                "id",
                "gradientUnits",
                "xml:lang",
                "gradientTransform",
                "xlink:type",
                "xlink:arcrole",
                "x1",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            ["set", "title", "animate", "animateTransform", "stop", "metadata", "desc"]
        ),
    ),
    "marker": SVGElement(
        "marker",
        attributes=frozenset(
            [
                "xml:space",
                "id",
                "xml:lang",
                "xml:base",
                "class",
                "style",
                "externalResourcesRequired",
                "viewBox",
                "preserveAspectRatio",
                "refX",
                "refY",
                "markerUnits",
                "markerWidth",
                "markerHeight",
                "orient",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "set",
                "text",
                "image",
                "font-face",
                "polyline",
                "marker",
                "animate",
                "font",
                "color-profile",
                "ellipse",
                "cursor",
                "style",
                "polygon",
                "title",
                "pattern",
                "circle",
                "radialGradient",
                "metadata",
                "defs",
                "symbol",
                "use",
                "animateMotion",
                "animateColor",
                "path",
                "line",
                "rect",
                "desc",
                "a",
                "g",
                "svg",
                "script",
                "mask",
                "altGlyphDef",
                "filter",
                "switch",
                "animateTransform",
                "linearGradient",
                "clipPath",
                "foreignObject",
                "view",
            ]
        ),
    ),
    "mask": SVGElement(
        "mask",
        attributes=frozenset(
            [
                "xml:base",
                "requiredExtensions",
                "xml:space",
                "height",
                "systemLanguage",
                "externalResourcesRequired",
                "maskContentUnits",
                "class",
                "style",
                "id",
                "width",
                "requiredFeatures",
                "xml:lang",
                "y",
                "x",
                "maskUnits",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "set",
                "text",
                "image",
                "font-face",
                "polyline",
                "marker",
                "animate",
                "font",
                "color-profile",
                "ellipse",
                "cursor",
                "style",
                "polygon",
                "title",
                "pattern",
                "circle",
                "radialGradient",
                "metadata",
                "defs",
                "symbol",
                "use",
                "animateMotion",
                "animateColor",
                "path",
                "line",
                "rect",
                "desc",
                "a",
                "g",
                "svg",
                "script",
                "mask",
                "altGlyphDef",
                "filter",
                "switch",
                "animateTransform",
                "linearGradient",
                "clipPath",
                "foreignObject",
                "view",
            ]
        ),
    ),
    "metadata": SVGElement(
        "metadata",
        attributes=frozenset(["xml:space", "xml:lang", "xml:base", "id"]),
        properties=empty_list,
        children=frozenset(["*"]),
    ),
    "missing-glyph": SVGElement(
        "missing-glyph",
        attributes=frozenset(
            [
                "xml:base",
                "xml:space",
                "id",
                "xml:lang",
                "class",
                "style",
                "d",
                "horiz-adv-x",
                "vert-origin-x",
                "vert-origin-y",
                "vert-adv-y",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "set",
                "text",
                "image",
                "font-face",
                "polyline",
                "marker",
                "animate",
                "font",
                "color-profile",
                "ellipse",
                "cursor",
                "style",
                "polygon",
                "title",
                "pattern",
                "circle",
                "radialGradient",
                "metadata",
                "defs",
                "symbol",
                "use",
                "animateMotion",
                "animateColor",
                "path",
                "line",
                "rect",
                "desc",
                "a",
                "g",
                "svg",
                "script",
                "mask",
                "altGlyphDef",
                "filter",
                "switch",
                "animateTransform",
                "linearGradient",
                "clipPath",
                "foreignObject",
                "view",
            ]
        ),
    ),
    "mpath": SVGElement(
        "mpath",
        attributes=frozenset(
            [
                "xlink:actuate",
                "xlink:show",
                "xml:base",
                "xml:space",
                "xlink:href",
                "id",
                "xlink:role",
                "xml:lang",
                "xlink:type",
                "xlink:title",
                "xlink:arcrole",
                "externalResourcesRequired",
            ]
        ),
        properties=empty_list,
        children=frozenset(["desc", "metadata", "title"]),
    ),
    "path": SVGElement(
        "path",
        attributes=frozenset(
            [
                "xml:base",
                "onmouseup",
                "onmouseout",
                "requiredExtensions",
                "onfocusout",
                "xml:space",
                "systemLanguage",
                "onmouseover",
                "pathLength",
                "externalResourcesRequired",
                "id",
                "onload",
                "style",
                "d",
                "onactivate",
                "onmousedown",
                "transform",
                "class",
                "requiredFeatures",
                "xml:lang",
                "onmousemove",
                "onclick",
                "onfocusin",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "animateMotion",
                "set",
                "title",
                "animateColor",
                "animateTransform",
                "animate",
                "desc",
                "metadata",
            ]
        ),
    ),
    "pattern": SVGElement(
        "pattern",
        attributes=frozenset(
            [
                "xlink:title",
                "xml:base",
                "requiredExtensions",
                "xml:space",
                "xlink:href",
                "height",
                "class",
                "systemLanguage",
                "patternContentUnits",
                "xlink:type",
                "externalResourcesRequired",
                "id",
                "xlink:actuate",
                "style",
                "xlink:show",
                "viewBox",
                "xlink:role",
                "width",
                "requiredFeatures",
                "patternUnits",
                "patternTransform",
                "y",
                "x",
                "preserveAspectRatio",
                "xlink:arcrole",
                "xml:lang",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "set",
                "text",
                "image",
                "font-face",
                "polyline",
                "marker",
                "animate",
                "font",
                "color-profile",
                "ellipse",
                "cursor",
                "style",
                "polygon",
                "title",
                "pattern",
                "circle",
                "radialGradient",
                "metadata",
                "defs",
                "symbol",
                "use",
                "animateMotion",
                "animateColor",
                "path",
                "line",
                "rect",
                "desc",
                "a",
                "g",
                "svg",
                "script",
                "mask",
                "altGlyphDef",
                "filter",
                "switch",
                "animateTransform",
                "linearGradient",
                "clipPath",
                "foreignObject",
                "view",
            ]
        ),
    ),
    "polygon": SVGElement(
        "polygon",
        attributes=frozenset(
            [
                "xml:base",
                "onmouseup",
                "onmouseout",
                "requiredExtensions",
                "onfocusout",
                "xml:space",
                "systemLanguage",
                "onmouseover",
                "externalResourcesRequired",
                "id",
                "onload",
                "style",
                "onactivate",
                "onmousedown",
                "transform",
                "class",
                "requiredFeatures",
                "points",
                "onmousemove",
                "onclick",
                "xml:lang",
                "onfocusin",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "animateMotion",
                "set",
                "title",
                "animateColor",
                "animateTransform",
                "animate",
                "desc",
                "metadata",
            ]
        ),
    ),
    "polyline": SVGElement(
        "polyline",
        attributes=frozenset(
            [
                "xml:base",
                "onmouseup",
                "onmouseout",
                "requiredExtensions",
                "onfocusout",
                "xml:space",
                "systemLanguage",
                "onmouseover",
                "externalResourcesRequired",
                "id",
                "onload",
                "style",
                "onactivate",
                "onmousedown",
                "transform",
                "class",
                "requiredFeatures",
                "points",
                "onmousemove",
                "onclick",
                "xml:lang",
                "onfocusin",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "animateMotion",
                "set",
                "title",
                "animateColor",
                "animateTransform",
                "animate",
                "desc",
                "metadata",
            ]
        ),
    ),
    "radialGradient": SVGElement(
        "radialGradient",
        attributes=frozenset(
            [
                "xlink:title",
                "xml:base",
                "fx",
                "fy",
                "xml:space",
                "xlink:href",
                "cy",
                "cx",
                "xlink:type",
                "externalResourcesRequired",
                "r",
                "id",
                "xlink:actuate",
                "gradientUnits",
                "style",
                "xlink:show",
                "spreadMethod",
                "class",
                "xlink:role",
                "xml:lang",
                "gradientTransform",
                "xlink:arcrole",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            ["set", "title", "animate", "animateTransform", "stop", "metadata", "desc"]
        ),
    ),
    "rect": SVGElement(
        "rect",
        attributes=frozenset(
            [
                "xml:base",
                "onmouseup",
                "onmouseout",
                "requiredExtensions",
                "onfocusout",
                "xml:space",
                "height",
                "systemLanguage",
                "onmouseover",
                "externalResourcesRequired",
                "id",
                "onload",
                "style",
                "ry",
                "onactivate",
                "onmousedown",
                "rx",
                "transform",
                "class",
                "width",
                "requiredFeatures",
                "xml:lang",
                "onmousemove",
                "onclick",
                "y",
                "x",
                "onfocusin",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "animateMotion",
                "set",
                "title",
                "animateColor",
                "animateTransform",
                "animate",
                "metadata",
                "desc",
            ]
        ),
    ),
    "script": SVGElement(
        "script",
        attributes=frozenset(
            [
                "xlink:actuate",
                "xlink:show",
                "xml:base",
                "xml:space",
                "xlink:href",
                "id",
                "xlink:role",
                "xml:lang",
                "xlink:type",
                "xlink:title",
                "xlink:arcrole",
                "type",
                "externalResourcesRequired",
            ]
        ),
        properties=empty_list,
        children=empty_list,
    ),
    "set": SVGElement(
        "set",
        attributes=frozenset(
            [
                "begin",
                "xlink:title",
                "xml:base",
                "requiredExtensions",
                "repeatCount",
                "xml:space",
                "xlink:href",
                "attributeName",
                "onbegin",
                "systemLanguage",
                "attributeType",
                "xlink:type",
                "externalResourcesRequired",
                "id",
                "restart",
                "fill",
                "xlink:actuate",
                "onload",
                "xlink:show",
                "end",
                "min",
                "repeatDur",
                "xlink:role",
                "to",
                "requiredFeatures",
                "xml:lang",
                "max",
                "dur",
                "xlink:arcrole",
                "onrepeat",
                "onend",
            ]
        ),
        properties=empty_list,
        children=frozenset(["desc", "metadata", "title"]),
    ),
    "stop": SVGElement(
        "stop",
        attributes=frozenset(
            ["xml:base", "xml:space", "xml:lang", "offset", "style", "class"]
        ),
        properties=presentation_attributes,
        children=frozenset(["animate", "set", "animateColor"]),
    ),
    "style": SVGElement(
        "style",
        attributes=frozenset(
            ["xml:lang", "xml:base", "title", "media", "xml:space", "type", "id"]
        ),
        properties=empty_list,
        children=frozenset(["*"]),
    ),
    "svg": SVGElement(
        "svg",
        attributes=frozenset(
            [
                "requiredExtensions",
                "onerror",
                "onfocusout",
                "xml:space",
                "height",
                "onscroll",
                "baseProfile",
                "contentStyleType",
                "id",
                "onabort",
                "onload",
                "style",
                "onmousedown",
                "onzoom",
                "onresize",
                "width",
                "version",
                "onmousemove",
                "onmouseup",
                "xmlns:xlink",
                "xmlns:ev",
                "onfocusin",
                "xml:base",
                "onclick",
                "onmouseout",
                "systemLanguage",
                "onmouseover",
                "externalResourcesRequired",
                "zoomAndPan",
                "class",
                "onunload",
                "xmlns",
                "onactivate",
                "viewBox",
                "requiredFeatures",
                "xml:lang",
                "y",
                "x",
                "preserveAspectRatio",
                "contentScriptType",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "set",
                "text",
                "image",
                "font-face",
                "polyline",
                "marker",
                "animate",
                "font",
                "color-profile",
                "ellipse",
                "cursor",
                "style",
                "polygon",
                "title",
                "pattern",
                "circle",
                "radialGradient",
                "metadata",
                "defs",
                "symbol",
                "use",
                "animateMotion",
                "animateColor",
                "path",
                "line",
                "rect",
                "desc",
                "a",
                "g",
                "svg",
                "script",
                "mask",
                "altGlyphDef",
                "filter",
                "switch",
                "animateTransform",
                "linearGradient",
                "clipPath",
                "foreignObject",
                "view",
            ]
        ),
    ),
    "switch": SVGElement(
        "switch",
        attributes=frozenset(
            [
                "xml:base",
                "onmouseup",
                "onmouseout",
                "requiredExtensions",
                "onfocusout",
                "xml:space",
                "systemLanguage",
                "onmouseover",
                "externalResourcesRequired",
                "class",
                "onload",
                "style",
                "onactivate",
                "onmousedown",
                "transform",
                "id",
                "requiredFeatures",
                "xml:lang",
                "onmousemove",
                "onclick",
                "onfocusin",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "set",
                "text",
                "image",
                "line",
                "use",
                "animateColor",
                "polyline",
                "path",
                "animate",
                "ellipse",
                "rect",
                "desc",
                "a",
                "animateMotion",
                "polygon",
                "g",
                "title",
                "svg",
                "switch",
                "animateTransform",
                "foreignObject",
                "circle",
                "metadata",
            ]
        ),
    ),
    "symbol": SVGElement(
        "symbol",
        attributes=frozenset(
            [
                "xml:base",
                "onmouseup",
                "onmouseout",
                "onfocusout",
                "xml:space",
                "onmouseover",
                "id",
                "externalResourcesRequired",
                "viewBox",
                "onload",
                "style",
                "onactivate",
                "onmousedown",
                "class",
                "xml:lang",
                "onmousemove",
                "onclick",
                "preserveAspectRatio",
                "onfocusin",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "set",
                "text",
                "image",
                "font-face",
                "polyline",
                "marker",
                "animate",
                "font",
                "color-profile",
                "ellipse",
                "cursor",
                "style",
                "polygon",
                "title",
                "pattern",
                "circle",
                "radialGradient",
                "metadata",
                "defs",
                "symbol",
                "use",
                "animateMotion",
                "animateColor",
                "path",
                "line",
                "rect",
                "desc",
                "a",
                "g",
                "svg",
                "script",
                "mask",
                "altGlyphDef",
                "filter",
                "switch",
                "animateTransform",
                "linearGradient",
                "clipPath",
                "foreignObject",
                "view",
            ]
        ),
    ),
    "text": SVGElement(
        "text",
        attributes=frozenset(
            [
                "xml:base",
                "onmouseup",
                "onmouseout",
                "requiredExtensions",
                "onfocusout",
                "xml:space",
                "class",
                "systemLanguage",
                "onmouseover",
                "dx",
                "dy",
                "externalResourcesRequired",
                "lengthAdjust",
                "onload",
                "style",
                "rotate",
                "onactivate",
                "onmousedown",
                "textLength",
                "transform",
                "id",
                "requiredFeatures",
                "xml:lang",
                "onmousemove",
                "onclick",
                "y",
                "x",
                "onfocusin",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "a",
                "animateMotion",
                "set",
                "title",
                "textPath",
                "tspan",
                "animateColor",
                "tref",
                "animateTransform",
                "altGlyph",
                "animate",
                "desc",
                "metadata",
            ]
        ),
    ),
    "textPath": SVGElement(
        "textPath",
        attributes=frozenset(
            [
                "requiredExtensions",
                "onfocusout",
                "xml:space",
                "xlink:href",
                "startOffset",
                "id",
                "onload",
                "style",
                "onmousedown",
                "lengthAdjust",
                "onmousemove",
                "onclick",
                "xlink:arcrole",
                "onfocusin",
                "xml:base",
                "onmouseup",
                "onmouseout",
                "xlink:title",
                "spacing",
                "systemLanguage",
                "onmouseover",
                "xlink:type",
                "externalResourcesRequired",
                "class",
                "xlink:actuate",
                "xlink:show",
                "onactivate",
                "textLength",
                "method",
                "xlink:role",
                "requiredFeatures",
                "xml:lang",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "a",
                "set",
                "title",
                "tspan",
                "animateColor",
                "tref",
                "altGlyph",
                "animate",
                "metadata",
                "desc",
            ]
        ),
    ),
    "title": SVGElement(
        "title",
        attributes=frozenset(
            ["style", "xml:lang", "xml:base", "xml:space", "class", "id"]
        ),
        properties=empty_list,
        children=frozenset(["*"]),
    ),
    "tref": SVGElement(
        "tref",
        attributes=frozenset(
            [
                "requiredExtensions",
                "onfocusout",
                "xml:space",
                "xlink:href",
                "id",
                "onload",
                "style",
                "onmousedown",
                "lengthAdjust",
                "onmousemove",
                "onclick",
                "xlink:arcrole",
                "onfocusin",
                "xml:base",
                "onmouseup",
                "onmouseout",
                "xlink:title",
                "systemLanguage",
                "onmouseover",
                "dx",
                "dy",
                "xlink:type",
                "externalResourcesRequired",
                "class",
                "xlink:actuate",
                "xlink:show",
                "onactivate",
                "textLength",
                "xlink:role",
                "requiredFeatures",
                "xml:lang",
                "y",
                "x",
                "rotate",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            ["set", "title", "animate", "metadata", "animateColor", "desc"]
        ),
    ),
    "tspan": SVGElement(
        "tspan",
        attributes=frozenset(
            [
                "xml:base",
                "onmouseup",
                "onmouseout",
                "requiredExtensions",
                "onfocusout",
                "xml:space",
                "class",
                "systemLanguage",
                "onmouseover",
                "dx",
                "dy",
                "externalResourcesRequired",
                "lengthAdjust",
                "onload",
                "style",
                "rotate",
                "onactivate",
                "onmousedown",
                "textLength",
                "id",
                "requiredFeatures",
                "xml:lang",
                "onmousemove",
                "onclick",
                "y",
                "x",
                "onfocusin",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "a",
                "set",
                "title",
                "tspan",
                "animateColor",
                "tref",
                "altGlyph",
                "animate",
                "metadata",
                "desc",
            ]
        ),
    ),
    "use": SVGElement(
        "use",
        attributes=frozenset(
            [
                "requiredExtensions",
                "onfocusout",
                "xml:space",
                "xlink:href",
                "height",
                "id",
                "onload",
                "style",
                "onmousedown",
                "transform",
                "width",
                "onmousemove",
                "onclick",
                "xlink:arcrole",
                "onfocusin",
                "xml:base",
                "onmouseup",
                "onmouseout",
                "xlink:title",
                "systemLanguage",
                "onmouseover",
                "xlink:type",
                "externalResourcesRequired",
                "class",
                "xlink:actuate",
                "xlink:show",
                "onactivate",
                "xlink:role",
                "requiredFeatures",
                "xml:lang",
                "y",
                "x",
            ]
        ),
        properties=presentation_attributes,
        children=frozenset(
            [
                "animateMotion",
                "set",
                "title",
                "animateColor",
                "animateTransform",
                "animate",
                "desc",
                "metadata",
            ]
        ),
    ),
    "view": SVGElement(
        "view",
        attributes=frozenset(
            [
                "xml:base",
                "viewTarget",
                "xml:space",
                "viewBox",
                "xml:lang",
                "preserveAspectRatio",
                "externalResourcesRequired",
                "zoomAndPan",
                "id",
            ]
        ),
        properties=empty_list,
        children=frozenset(["desc", "metadata", "title"]),
    ),
    "vkern": SVGElement(
        "vkern",
        attributes=frozenset(
            ["xml:base", "g2", "g1", "xml:space", "u1", "u2", "xml:lang", "id", "k"]
        ),
        properties=empty_list,
        children=empty_list,
    ),
}
